mod = 10


def fib(n):

    fibs = []

    fibs.append(0)
    fibs.append(1)

    for i in range(2, n+1):
        fibo = (fibs[i-1] + fibs[i-2]) % mod
        fibs.append(fibo)

    return fibs[n] % mod

n = int(input())
print(fib(n))
