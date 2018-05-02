#
# Indices of parent, left child, right child
#

class Heap(object):
    def __init__(self, arr):
        self.A = arr
        self.length = len(self.A)
        self.max_index = self.length - 1

    def parent(self, i):
        """
        Return parent node of a node at index 'i'
        """
        return (i+1)/2 - 1
        # Or right shift
        # return i >> 1

    def left(self, i):
        """
        Return left child of a node at index 'i'
        """
        return 2*(i+1) - 1
        # Or left shit
        # return i << 1

    def right(self, i):
        """
        Return Right child of a node at index 'i'
        """
        return 2*(i+1)
        # Or left shift and add 1
        # return (i << 1) + 1

class MaxHeap(Heap):
    def is_max_heap(self, i):
        """
        Value of a node is at most the value of its parent
        """
        return self.A[self.parent(i)] >= self.A[i]

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        # Find the largest of parent, left and right
        if l <= self.max_index and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r <= self.max_index and self.A[r] > self.A[largest]:
            largest = r

        # Parent is not the largest, violates Max-Heap property
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)
        return True

    def build_max_heap(self):
        """
        Convert an array into a Max Heap using max_heapify method.
        Goes through all non-leaf nodes and calls max-heapify
        All leaf nodes of complete binary tree are : A[(n/2 + 2) .. n]
        All non-leaf nodes of complete binary tree are: A[1..(n/2)]
        """
        for i in xrange(self.max_index / 2, -1, -1):
            self.max_heapify(i)
        return True


class MinHeap(Heap):
    def is_min_heap(self, i):
        """
        Value of a node is at least the value of its parent
        """
        return self.A[self.parent(i)] <= self.A[i]
