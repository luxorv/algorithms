import sys

def get_change(n):

    coins, i = (0, 0)
    denominations = [10, 5, 1]

    while n > 0 and i <= len(denominations):
        while denominations[i] <= n:
            print("{} money left now minus {}".format(n, denominations[i]))
            n -= denominations[i]
            coins += 1

        i += 1

    return coins


if __name__ == '__main__':
    n = int(input())
    print(get_change(n))
