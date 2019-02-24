
import numpy as np

from heap import Heap
from ball_tree import BallTree, euclid_metric, knn
from data_manipulation import prepare_data

class Classifier:
  def __init__(self, training_data_size_ratio: float, k: int = 5):
    # Split dataset into training and testing data
    self.k = k
    self.dataset = prepare_data().values
    np.random.shuffle(self.dataset)
    size = int(len(self.dataset) * training_data_size_ratio)
    # Get the labels(unique values situated on the last column in the dataset)
    self.classes = set(self.dataset[:, -1])

    result_col = self.dataset.shape[1] - 1  
    self.training_data = Classifier.create_classes(self.dataset[:size], result_col, self.classes)
    self.test_data = Classifier.create_classes(self.dataset[size:], result_col, self.classes)

    # build the trees for each class in the training set
    self.training_trees = dict((class_, BallTree(data, euclid_metric)) for class_, data in self.training_data.items())

  # Returns a heap of dictionaries like {point, class, distance}
  def predict(self, point):
    votes = dict((class_, 0) for class_ in self.classes)
    cmp = lambda parent, child: parent['distance'] > child['distance']
    result = Heap(cmp)
    # Calculate knn for each class
    partials = dict((class_, knn(tree, point, self.k, euclid_metric)) for class_, tree in self.training_trees.items())
    # Merge the partial results in one heap
    for class_, heap in partials.items():
      for (point, distance) in heap:
        if len(result) < self.k or distance < result[0]['distance']:
          result.push({'point': point, 'distance': distance, 'class': class_})
        if len(result) > self.k:
          result.pop()
    for item in result:
      votes[item['class']] += 1
    # Return the class with the highest value in the dictionary
    return max(votes, key=votes.get)

  def test(self):
    correct = 0
    total = 0
    for class_ in self.test_data:
      for point in self.test_data[class_]:
        prediction = self.predict(point)
        if prediction == class_:
          correct += 1
        total += 1
    return correct / total


  @staticmethod
  def create_classes(data: np.array, result_col: int, classes: set):
    # One line chonker
    # Create a class for each result possibility(in this case only 0 and 1)
    # with all the data that lead to the given result(the key)
    return dict((class_, data[np.where(data[:, result_col] == class_)][:, :-1]) for class_ in classes)

if __name__ == '__main__':
  for ratio in [.1 * r for r in range(5, 10)]:
    for k in [3, 5, 7]:
      print('ratio = %s and k = %s' % (ratio, k))
      for i in range(5):
        classifier = Classifier(ratio, k)
        accuracy = classifier.test()
        print('Accuracy of the knn classifier at step %s is: %s.' % (i, accuracy))