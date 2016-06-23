"""Binary search algorithm."""
import random
import sys


def binarysearch(array, key):
    """Perform binary search on sorted array.
    
    Args:
        array - list of elements to be searched for key
        key - element to be searched in the array
    """
    low, high = 0, len(array) - 1
    while low <= high:
	mid = low + (high - low) / 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def isSorted(array):
    """Check if array is sorted in ascending order."""
    for i in xrange(len(array) - 1):
         if array[i] > array[i + 1]:
             return False
    return True


if __name__ == '__main__':
   array = [-sys.maxint-1, 0, -99, 1, sys.maxint, 40, 22, 11, 1, 1]
   array = sorted(array)
   
   assert isSorted(array)
   k = 40
   
   print "Array to be searched"
   print array

   print "Found key {} ?".format(k)
   result = binarysearch(array, k)
   print "No" if result == -1 else "Yes at position {}".format(result + 1)

   k = 999
   print "Found key {} ?".format(k)
   result = binarysearch(array, k)
   print "No" if result == -1 else "Yes at position {}".format(result + 1)
