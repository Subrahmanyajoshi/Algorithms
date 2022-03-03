class KnapSack(object):

    @staticmethod
    def get_optimal_value(capacity, weights, values):
        knapsack_value = 0
        unit_values = [a / b for a, b in zip(values, weights)]
        zipped = zip(unit_values, weights, values)
        unit_values, weights, values = zip(*sorted(zipped, reverse=True))

        for i in range(len(unit_values)):
            unit_value = unit_values[i]
            weight = weights[i]

            while capacity > 0 and weight > 0:
                capacity -= 1
                knapsack_value += unit_value
                weight -= 1

        return knapsack_value


if __name__ == "__main__":
    capacity = 50
    weights = [20, 50, 30]
    values = [60, 100, 120]

    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # v = data[2:(2 * n + 2):2]
    # w = data[3:(2 * n + 2):2]
    # opt_value = get_optimal_value(capacity, w, v)
    opt_value = KnapSack.get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
