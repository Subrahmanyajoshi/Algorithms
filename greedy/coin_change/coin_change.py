import sys


def get_change(amount):
    num_coins = 0
    coin_values = [10, 5, 1]

    for coin in coin_values:
        num_coins += int(amount / coin)
        amount = amount % coin
        if amount == 0:
            return num_coins

    return num_coins


if __name__ == '__main__':
    money = int(input())
    print(get_change(amount=money))
