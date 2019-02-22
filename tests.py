import numpy as np
import matplotlib.pyplot as plt

from functools import cmp_to_key
from heap import Heap
from ball_tree import BallTree, euclid_metric

if __name__ == '__main__':
  plt.title = 'KNN search.'
  points = np.random.randint(100, size=(20, 2))

  plt.rcParams["font.size"] = 1
  x = points[:, 0]
  y = points[:, 1]
  plt.scatter(x, y)

  tree = BallTree(points, euclid_metric)
  point = np.random.randint(0, 100, 2)
  x_, y_ = point
  plt.plot(x_, y_, 'bo', color='red')
  
  distances = sorted([euclid_metric(point, candidate) for candidate in points])
  s = set(distances)

  k = 10
  cmp = lambda a, b: a[1] > b[1]
  heap = Heap(cmp)
  for candidate in points:
    distance = euclid_metric(point, candidate)
    if len(heap) < k or distance < heap[0][1]:
      heap.push((candidate, distance))
    if len(heap) > k:
      heap.pop()
  for candidate in heap:
    print(candidate)
    x_, y_ = candidate[0]
    plt.plot(x_, y_, 'bo', color='pink')

  print(distances[:k])
  all = True
  for candidate in heap:
    if not candidate[1] in s:
      all = False
      break
  print('All? %s' % all)
  plt.show()