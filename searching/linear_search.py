from typing import List


class LinearSearch(object):

    def __init__(self, array: List, element: int):
        self.array = array
        self.element = element

    def search(self):
        for i in range(len(self.array)):
            if self.array[i] == self.element:
                return i
        return "Not Found"


def main():
    array = [10, 45, 1, 8, 56, 400, 360]
    search_number = 8

    linear_search = LinearSearch(array=array, element=search_number)
    print(linear_search.search())


if __name__ == '__main__':
    main()
