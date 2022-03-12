# Using a dictionary to make fibonacci number computation faster

def calc_fib(n, computed):
    if n <= 1:
        return n
    if n not in computed:
        computed[n] = calc_fib(n - 1, computed=computed) + calc_fib(n - 2, computed=computed)
    return computed[n]


def main():
    n = int(input())
    print(calc_fib(n, computed={0: 0, 1: 1}))


if __name__ == '__main__':
    main()
