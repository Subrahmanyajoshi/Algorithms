class MaxAdRevenue(object):

    @staticmethod
    def max_ad_revenue(a, b):
        a = sorted(a, reverse=True)
        b = sorted(b, reverse=True)
        return sum([x * y for x, y in zip(a, b)])


if __name__ == '__main__':

    a = [1, 3, -5]
    b = [-2, 4, 1]

    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # a = data[1:(n + 1)]
    # b = data[(n + 1):]
    print(MaxAdRevenue.max_ad_revenue(a, b))
