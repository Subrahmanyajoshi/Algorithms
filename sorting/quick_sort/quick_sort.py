from typing import List


class QuickSort(object):

    def __init__(self, array: List):
        self.array = array

    def swap(self, first_idx: int, second_idx: int):
        temp = self.array[first_idx]
        self.array[first_idx] = self.array[second_idx]
        self.array[second_idx] = temp

    def partition(self, left: int, right: int):
        pivot = self.array[left]
        j = left
        for i in range(left + 1, right+1):
            if self.array[i] <= pivot:
                j += 1
                self.swap(first_idx=i, second_idx=j)
        self.swap(first_idx=left, second_idx=j)
        return j

    def sort(self, left: int, right: int):
        if left >= right:
            return

        m = self.partition(left=left, right=right)
        self.sort(left=left, right=m - 1)
        self.sort(left=m + 1, right=right)


def main():
    array = [10, 17, 200, 11, 3]

    quick_sort = QuickSort(array=array)
    quick_sort.sort(left=0, right=len(array)-1)
    print("Sorted array: \n", quick_sort.array)


if __name__ == '__main__':
    main()
