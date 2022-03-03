from typing import List


class SelectionSort(object):

    def __init__(self, array: List):
        self.array = array
        self.len = len(array)

    def swap(self, first_idx: int, second_idx: int):
        temp = self.array[first_idx]
        self.array[first_idx] = self.array[second_idx]
        self.array[second_idx] = temp

    def find_min(self, start, end):
        min_idx = start
        for k in range(start, end):
            if self.array[k] < self.array[min_idx]:
                min_idx = k
        return min_idx

    def run(self):
        for i in range(self.len - 1):
            i_min = i
            j_min = self.find_min(start=i+1, end=self.len)
            if self.array[j_min] < self.array[i_min]:
                self.swap(first_idx=i_min, second_idx=j_min)


def main():
    array = [9, 7, 3, 48, 1, 2, 1, 3]
    selection_sort = SelectionSort(array=array)
    selection_sort.run()
    print("Sorted array: \n", selection_sort.array)


if __name__ == '__main__':
    main()
