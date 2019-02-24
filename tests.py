from functools import cmp_to_key

import matplotlib.pyplot as plt
import numpy as np

from ball_tree import BallTree, euclid_metric, knn
from heap import Heap

def traverse(node, plt):
  if node is not None:
    if node.is_leaf:
      x, y = node.center
      plt.plot(x, y, 'bo', color='cyan')
    traverse(node.left, plt)
    traverse(node.right, plt)

if __name__ == '__main__':
  count = 100
  plt.title = 'KNN search.'
  points = np.random.randint(1000, size=(count, 2))

  plt.rcParams["font.size"] = 1
  x = points[:, 0]
  y = points[:, 1]
  plt.scatter(x, y)

  point = np.random.randint(0, count, 2)
  x_, y_ = point
  plt.plot(x_, y_, 'bo', color='red')

  k = 10
  cmp = lambda a, b: a[1] > b[1]
  heap = Heap(cmp)
  
  distances = sorted([euclid_metric(point, candidate) for candidate in points])
  distances = distances[:k]
  s = set(distances)

  for candidate in points:
    distance = euclid_metric(point, candidate)
    if len(heap) < k or distance < heap[0][1]:
      heap.push((candidate, distance))
    if len(heap) > k:
      heap.pop()
  for candidate in heap:
    # print(candidate)
    x_, y_ = candidate[0]
    plt.plot(x_, y_, 'bo', color='pink')

  print(distances)
  all = True
  for candidate in heap:
    if not candidate[1] in s:
      all = False
      break
  print('All found in the brute force approach? %s' % all)
  
  tree = BallTree(points, euclid_metric)
  distance_balls = knn(tree, point, k, euclid_metric)
  # print(len(distance_balls))
  # print(distance_balls)

  all = True
  for candidate in distance_balls:
    x, y = candidate[0]
    plt.plot(x, y, 'bo', color='#00ff00')
    if not candidate[1] in s:
      all = False
      break
  print('All found in the ball tree approach?   %s' % all)

  # traverse(tree, plt)
  plt.show()