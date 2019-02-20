from numpy.random import randint

class Heap:
  # @param cmp(parent, child) -> parent < child => min heap
  def __init__(self, cmp):
    assert cmp is not None, 'No compare function provided'
    self.container = list()
    self.cmp = cmp

  def __len__(self):
    return len(self.container)

  def __repr__(self):
    return 'Heap: %s' % self.container

  def _parent(self, index):
    return (index - 1) >> 1

  def _left(self, index):
    return 2 * index + 1

  def _right(self, index):
    return 2 * index + 2

  def _heapify(self, index):
    left = self._left(index)
    right = self._right(index)
    next = None
    current = self.container[index]

    if left < len(self.container) and not self.cmp(current, self.container[left]):
      next = left
    if right < len(self.container) and not self.cmp(current, self.container[right]):
      next = right
      if not self.cmp(self.container[right], self.container[left]):
        next = left

    if next is not None:
      child = self.container[next]
      self.container[next] = current
      self.container[index] = child
      self._heapify(next)

  def push(self, item):
    self.container.append(item)
    index = len(self.container) - 1

    while index > 0:
      parent_index = self._parent(index)
      current = self.container[index]
      parent = self.container[parent_index]
      if not self.cmp(parent, current):
        self.container[parent_index] = current
        self.container[index] = parent
        index = parent_index
      else:
        break

  def pop(self):
    if len(self.container) > 0:
      last = self.container.pop()
      if len(self.container) > 0:
        first = self.container[0]
        self.container[0] = last
        self._heapify(0)
        return first
      else:
        return last
    return None

  def make_heap(self):
    index = len(self.container) >> 1
    while index > 0:
      self._heapify(index)
      index -= 1


if __name__ == '__main__':
  heap = Heap(cmp = lambda parent, child: parent < child)
  for nbr in randint(0, 30, 5):
    heap.push(nbr)
  print(repr(heap))
  heap.pop()
  print(repr(heap))
