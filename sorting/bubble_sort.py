from typing import List


class BubbleSort(object):

    def __init__(self, array: List):
        self.array = array
        self.len = len(array)

    def swap(self, first_idx: int, second_idx: int):
        temp = self.array[first_idx]
        self.array[first_idx] = self.array[second_idx]
        self.array[second_idx] = temp

    def run(self):
        for i in range(self.len - 1):
            no_swap = True
            print(self.array)
            for j in range(self.len - 2):
                if self.array[j + 1] < self.array[j]:
                    no_swap = False
                    self.swap(j + 1, j)
            if no_swap:
                break


def main():
    array = [9, 7, 2, 1, 3]
    bubble_sort = BubbleSort(array=array)
    bubble_sort.run()
    print("Sorted array: \n", bubble_sort.array)


if __name__ == '__main__':
    main()
