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

def manhattan_metric(a, b):
  return np.sum(np.abs(a - b))

def euclid_metric(a, b):
  return np.sqrt(np.sum(np.power(np.subtract(a, b), 2)))

class BallTree:
  def __init__(self, points: [[float]], metric):
    if points is None:
      raise ValueError('Dataset not provided.')
    self.is_leaf = True
    self.left = self.right = None

    if len(points) == 1:
      self.radius = 0
      self.points = np.array(points, copy=True)
      self.center = self.points[0]
      return None

    mid = len(points) >> 1
    self.is_leaf = False
    # Computing the dimension of the greatest spread, i.e.
    # the dimension of points from the dataset that
    # spread over the largest interval
    self.dimension = np.argmax(points.max(0) - points.min(0))
    # Compute radius given the metric passed as an argument
    # The metric is used to calculate the distance between 2 points
    # Using the partition method which is a wrapper over the quick-select
    # algorithm.
    center_index = introselect_by_dimension(points, mid, self.dimension)
    self.center = points[center_index]
    self.radius = np.apply_along_axis(lambda point: metric(self.center, point), 1, points).max(0)

    left = points[:mid]
    right = points[mid:]

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

def _knn_search(node, target, k, metric, queue):
  distance = metric(node.center, target)
  if len(queue) == k and distance - node.radius > queue[0][1]:
    return
  elif node.is_leaf:
    # Each leaf node consists of only one point.
    point = node.center
    distance = metric(point, target)
    if len(queue) < k or distance < queue[0][1]:
      queue.push((point, distance))
      if len(queue) > k:
        queue.pop()
  else:
    # Recurse on the child whose center is closes
    # to the target point. This way we might prune
    # some parts of the tree branches
    left = node.left
    right = node.right
    if metric(right.center, target) < metric(left.center, target):
      left, right = right, left
    _knn_search(left, target, k, metric, queue)
    _knn_search(right, target, k, metric, queue)

def knn(node, target, k, metric):
  cmp = lambda a, b: a[1] > b[1]
  queue = Heap(cmp)
  _knn_search(node, target, k, metric, queue)
  return queue
