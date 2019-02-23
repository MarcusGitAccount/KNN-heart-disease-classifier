
import numpy as np
import pandas as pd

from os import path

def prepare_data():
  paths = [
    path.join('data', 'processed.cleveland.data.txt'),
    path.join('data', 'processed.hungarian.data.txt'),
    path.join('data', 'processed.switzerland.data.txt'),
    path.join('data', 'processed.va.data.txt')
  ]
  # read each of the four databases
  tables = list(map(lambda path: pd.read_csv(path, delimiter=',', header=None), paths))
  # merge databases
  dataset = pd.concat(tables).apply(pd.to_numeric, errors='coerce')
  means = np.nanmean(a=dataset.values, axis=0)

  # knn cannot work with nan values so we replace each nan occurence with
  # its column mean equivalent
  for index, column in enumerate(dataset):
    dataset[column] = dataset[column].fillna(means[index])
  last_column = dataset.columns[-1]
  # the #58 attribute in the processed datafiles has a binary value only
  # the values 2, 3, 4 are reminiscent of the before parsing data
  dataset[last_column] = dataset[last_column].replace([2, 3, 4], 1)
  return dataset

if __name__ == '__main__':
  dataset = prepare_data()
  print(dataset)