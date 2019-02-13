import numpy as np
import matplotlib.pyplot as plt
from functools import cmp_to_key

# Introselect is a hybrid algorithm, combining both quickselect
# and median of medians
# Given an array of points find the point with 
# the kth largest dimension givne
def introselect_by_dimension(points: [[]], kth, dimension):
  partial_sorted = np.argpartition(points, kth, axis=0)
  index = partial_sorted[kth][dimension]
  return index

def euclid_metric(a, b):
  return np.sqrt(np.sum(np.power(np.subtract(a, b), 2)))

class BallTree:
  def __init__(self, points: [[float]], metric):
    if points is None:
      raise ValueError('Dataset not provided.')
    self.center = self.radius = None
    self.dimension = None
    self.left  = None
    self.right = None
    self.points = np.array(points, copy=True)

    if len(points) <= 1:
      return None

    mid = len(self.points) >> 1
    # Computing the dimension of the greatest spread, i.e.
    # the dimension of points from the dataset that
    # spread over the largest interval
    self.dimension = np.argmax(self.points.max(0) - self.points.min(0))
    # Compute radius given the metric passed as an argument
    # The metric is used to calculate the distance between 2 points
    # Using the partition method which is a wrapper over the quick-select
    # algorithm.
    center_index = introselect_by_dimension(points, mid, self.dimension)
    self.center = self.points[center_index]
    self.radius = np.apply_along_axis(lambda point: metric(self.center, point), 1, self.points).max(0)
    self.left  = BallTree(self.points[:mid], metric)
    self.right = BallTree(self.points[mid:], metric)

  def plot(self, plt):
    if len(self.points) > 1:
      circle = plt.Circle(xy=self.center, radius=self.radius, fill=False)
      plt.gcf().gca().add_artist(circle)

  def print(self):
    print(self.center, self.radius, self.dimension)
    print(self.points, end="\n\n")

def traverse_tree(tree_node, plt=None): 
  if tree_node is not None:
    if plt is not None and tree_node.center is not None:
      tree_node.plot(plt)
    traverse_tree(tree_node.left, plt)
    traverse_tree(tree_node.right, plt)

points = np.random.rand(1000, 10) * 10000

# plt.rcParams["font.size"] = 1
# x = points[:, 0]
# y = points[:, 1]

# plt.scatter(x, y)
# plt.show()

tree = BallTree(points, euclid_metric)



