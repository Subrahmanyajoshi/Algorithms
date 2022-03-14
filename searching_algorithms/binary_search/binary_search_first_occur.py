import math
from typing import List


class BinarySearch(object):

    def __init__(self, array: List, key: int):
        self.array = array
        self.key = key
        self.first_index = len(array)

    def search(self, low, high):
        if high < low:
            return -1
        mid = math.floor(low + ((high - low) / 2))

        if self.array[mid] == self.key:
            if mid < self.first_index:
                self.first_index = mid

        if self.key <= self.array[mid]:
            return self.search(low=low, high=mid - 1)
        else:
            return self.search(low=mid + 1, high=high)


def main():
    # Binary search requires that the input array is sorted.

    array = [2, 4, 4, 4, 7, 7, 9]
    keys = [9, 4, 5, 2]
    results = []

    for key in keys:
        binary_search = BinarySearch(array=array, key=key)
        _ = binary_search.search(0, len(array) - 1)
        results.append(binary_search.first_index)
    print(results)


if __name__ == '__main__':
    main()
