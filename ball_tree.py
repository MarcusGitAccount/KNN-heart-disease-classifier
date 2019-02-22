import numpy as np
import matplotlib.pyplot as plt

from functools import cmp_to_key
from heap import Heap

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
    self.is_leaf = True
    self.center = self.radius = None
    self.dimension = None
    self.left  = None
    self.right = None
    self.points = np.array(points, copy=True)

    if len(points) == 1:
      self.center = self.points[0]
      return None

    mid = len(self.points) >> 1
    self.is_leaf = False
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

    left = self.points[:mid]
    right = self.points[mid:]

    if len(left) != 0:
      self.left = BallTree(left, metric)
    if len(right) != 0:
      self.right = BallTree(right, metric)

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

def _knn_update(node, target, metric):
  pass

def _knn_prepare(node, target, k, metric):
  pass

def knn_search(node, target, k, metric, queue):
  if len(queue) != 0:
    if metric(node.pivot, target) > metric():
     pass