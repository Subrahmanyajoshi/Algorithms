import sys
from typing import List


class LargestNumber(object):

    @staticmethod
    def repeat_to_length(s, wanted):
        return (s * (wanted // len(s) + 1))[:wanted]

    @staticmethod
    def compare(num1, num2):
        num1_len = len(num1)
        num2_len = len(num2)

        max_len = num1_len if num1_len > num2_len else num2_len
        nums = {num1: LargestNumber.repeat_to_length(num1, max_len),
                num2: LargestNumber.repeat_to_length(num2, max_len)}

        if nums[num1] == nums[num2]:
            return num1

        i = 0
        while i < max_len:

            if nums[num1][i] == nums[num2][i]:
                i += 1
                continue

            if nums[num1][i] > nums[num2][i]:
                return num1
            else:
                return num2

    @staticmethod
    def largest_number(values: List):

        a = [str(value) for value in values]
        res = ""

        while len(a) != 0:

            if len(a) == 1:
                res += a[0]
                break

            max_value = a[0]
            for value in a[1:]:
                max_value = LargestNumber.compare(max_value, value)
            res += max_value
            max_index = a.index(max_value)
            _ = a.pop(max_index)

        return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]

    # a = [21, 2]
    # a = [9, 4, 6, 1, 9]
    # a = [22, 80, 80, 71]
    a = [10, 0, 20, 0, 18]
    print(LargestNumber.largest_number(a))
