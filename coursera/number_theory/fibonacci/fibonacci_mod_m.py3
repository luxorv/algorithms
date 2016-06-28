def get_fibonaccihuge(n, m):

    fibs = []

    fibs.append(0)
    fibs.append(1)

    i = 2

    while True:
        fibo = (fibs[i-1] + fibs[i-2]) % m
        fibs.append(fibo)

        if fibs[i-1] is 0 and fibs[i] is 1:
            break

        i += 1

    pisano_period = len(fibs) - 2
    actual_n = n % pisano_period

    return fibs[actual_n] % m


n, m = map(int, input().split())
print(get_fibonaccihuge(n, m))
