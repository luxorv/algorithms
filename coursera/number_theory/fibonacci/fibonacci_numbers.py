from random import randint
from time import time


def naive_fib(n):
    if (n <= 1):
        return n

    return naive_fib(n - 1) + naive_fib(n - 2)

mod = 10


def fib(n):

    fibs = []

    fibs.append(0)
    fibs.append(1)

    for i in range(2, n+1):
        fibo = (fibs[i-1] + fibs[i-2]) % mod
        fibs.append(fibo)

    return fibs[n]


def test():

    while True:
        n = randint(0, 20)

        naive = naive_fib(n)
        fast_fib = fib(n)

        if naive != fast_fib:
            print("Wrong Answer, N: {} - naive: {} vs fast: {}"
                  .format(n, naive, fast_fib))
            break
        else:
            print('Ok N: {} - Fib: {}'.format(n, fast_fib))


if __name__ == '__main__':
    # test()
    now = time()
    fibs = fib(3) % 10
    seconds = time() - now
    print("time: ", seconds, fibs)
