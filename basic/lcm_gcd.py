
def gcd_naive(n1, n2):
    while n2 != 0:
        t = n2
        n2 = n1 % n2
        n1 = t
    return n1


def lcm_naive(a, b):
    gcd = gcd_naive(a, b)
    lcm = (a*b)/gcd
    return int(lcm)


def main():
    a, b = map(int, input().split())
    print("GCD: ", gcd_naive(a, b))
    print("LCM: ", lcm_naive(a, b))


if __name__ == '__main__':
    main()
