"""Code for Quicksort using Hoare partition scheme."""

import random
import sys


def qsort(array, low, high):
    """Run quick sort algorithm on partitions."""
    if low < high:
        p = partition(array, low, high)
        qsort(array, low, p)
        qsort(array, p + 1, high)


def partition(array, low, high):
    """Find the partition position."""
    i, j = low, high - 1
    pivot = array[low]

    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def isSorted(array):
    """Check if array is sorted in ascending order."""
    for i in xrange(len(array) - 1):
         if array[i] > array[i + 1]:
             return False
    return True


if __name__ == '__main__':
    n = 20
    array =  [random.randint(-sys.maxint - 1, sys.maxint) for _ in xrange(n)]
    print 'Original array'
    print array

    print 'After sorting'
    qsort(array, 0, len(array))
    print array

    assert isSorted(array)
