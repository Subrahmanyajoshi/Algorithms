import sys
from typing import List


class LargestNumber(object):

    @staticmethod
    def compare(num1, num2):
        max_num = num1
        num1_len = len(num1)
        num2_len = len(num2)

        min_len = num1_len if num1_len > num2_len else num2_len
        for i in range(min_len):
            if num2[i] > num1[i]:
                max_num = num2
        return int(max_num)

    @staticmethod
    def largest_number(a: List):
        res = ""
        while len(a) != 0:
            max_value = a[0]
            for value in a:
                max_value = LargestNumber.compare(str(value), str(max_value))
            res += str(max_value)
            max_index = a.index(max_value)
            _ = a.pop(max_index)

        return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]

    a = [21, 2]
    print(LargestNumber.largest_number(a))
