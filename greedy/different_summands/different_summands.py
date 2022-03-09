import sys


class DifferentSummands(object):

    @staticmethod
    def optimal_summands(n):
        summands = []
        total_sum = 0
        i = 0
        while total_sum < n:
            i += 1
            if total_sum+i > n:
                diff = n - total_sum
                summands[-1] += diff
            else:
                summands.append(i)
            total_sum += i

        return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)

    # n = 20
    summands = DifferentSummands.optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
