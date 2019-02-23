
import numpy as np

from ball_tree import BallTree, knn, euclid_metric
from data_manipulation import prepare_data

class Classifier:
  def __init__(self, training_data_size_ratio: float, k: int = 5):
    # Split dataset into training and testing data
    self.dataset = prepare_data().values
    size = int(len(self.dataset) * training_data_size_ratio)
    # Get the labels(unique values situated on the last column in the dataset)
    self.classes = set(self.dataset[:, -1])

    result_col = self.dataset.shape[1] - 1  
    self.training_data = Classifier.create_classes(self.dataset[:size], result_col, self.classes)
    self.test_data = Classifier.create_classes(self.dataset[size:], result_col, self.classes)

  @staticmethod
  def create_classes(data: np.array, result_col: int, classes: set):
    # One line chonker
    # Create a class for each result possibility(in this case only 0 and 1)
    # with all the data that lead to the given result(the key)
    return dict((class_, data[np.where(data[:, result_col] == class_)][:, :-1]) for class_ in classes)

if __name__ == '__main__':
  classifier = Classifier(.8, k=5)