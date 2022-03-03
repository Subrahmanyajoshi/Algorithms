from typing import List


class MergeSort(object):

    @staticmethod
    def merge(b, c):
        merged_list = list()
        while len(b) != 0 and len(c) != 0:
            if b[0] < c[0]:
                min_element = b.pop(0)
            else:
                min_element = c.pop(0)
            merged_list.append(min_element)
        if len(b) != 0:
            merged_list = merged_list + b

        if len(c) != 0:
            merged_list = merged_list + c

        return merged_list

    @staticmethod
    def sort(a: List):
        n = len(a)
        if n < 2:
            return a
        mid = int(n / 2)
        left = list()
        right = list()

        for i in range(mid):
            left.append(a[i])
        for j in range(mid, n):
            right.append(a[j])

        b = MergeSort.sort(left)
        c = MergeSort.sort(right)
        a_merged = MergeSort.merge(b, c)

        return a_merged


def main():
    array = [0, 17, 2, 11, 3]
    sorted_array = MergeSort.sort(array)
    print("Sorted array: \n", sorted_array)


if __name__ == '__main__':
    main()
