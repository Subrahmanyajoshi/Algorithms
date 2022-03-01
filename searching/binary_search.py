import math
from typing import List


class BinarySearch(object):

    def __init__(self, array: List, key: int):
        self.array = array
        self.key = key

    def search(self, low, high):
        if high < low:
            return "Not Found"
        mid = math.floor(low + ((high - low) / 2))

        if self.array[mid] == self.key:
            return mid

        if self.key < self.array[mid]:
            return self.search(low=low, high=mid-1)
        else:
            return self.search(low=mid+1, high=high)


def main():

    # Binary search requires that the input array is sorted.
    array = [1, 8, 10, 45, 56, 360, 400]
    key = 56

    binary_search = BinarySearch(array=array, key=key)
    print(binary_search.search(0, len(array) - 1))


if __name__ == '__main__':
    main()
