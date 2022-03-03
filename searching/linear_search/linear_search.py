from typing import List


class LinearSearch(object):

    def __init__(self, array: List, key: int):
        self.array = array
        self.key = key

    def search(self):
        for i in range(len(self.array)):
            if self.array[i] == self.key:
                return i
        return "Not Found"


def main():
    array = [10, 45, 1, 8, 56, 400, 360]
    key = 45

    linear_search = LinearSearch(array=array, key=key)
    print(linear_search.search())


if __name__ == '__main__':
    main()
