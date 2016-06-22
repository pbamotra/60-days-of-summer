"""Merge sort algorithm."""
from heapq import merge
import random
import sys


def mergesort(array):
    """Implementation of merge sort algorithm."""
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = mergesort(left)
    right = mergesort(right)
    
    return list(merge(left, right))


def isSorted(array):
    """Check if array is sorted in ascending order."""
    for i in xrange(len(array) - 1):
         if array[i] > array[i + 1]:
             return False
    return True


if __name__ == '__main__':
   if len(sys.argv) < 2:
       print "Usage: python t21062016-mergesort.py [N >= 0]"
       sys.exit(1)

   n = int(sys.argv[1])
   array = [random.randint(-sys.maxint - 1, sys.maxint) for _ in xrange(n)]

   print "Before sorting"
   print array

   print "After sorting"
   sorted_array = mergesort(array)
   print sorted_array

   assert isSorted(sorted_array)
