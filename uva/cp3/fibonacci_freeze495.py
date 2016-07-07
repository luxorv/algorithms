import sys

fib = list(range(5011))
fib[0] = 0
fib[1] = 1

for i in range(2, 5011):
    fib[i] = fib[i-1] + fib[i-2]

for line in sys.stdin.readlines():
    n = int(line.split()[0])
    print("The Fibonacci number for {} is {}".format(n, fib[n]))
