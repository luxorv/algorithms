inp = input().split()

i = int(inp[0])
j = int(inp[1])

cycles = [-1] * 1000000


def cycle_of_length(n):
    n = int(n)

    if cycles[n] != -1:
        return cycles[n]

    cnt = 0

    while True:

        n = int(n)
        cnt += 1

        if n == 1:
            cycles[n] = cnt
            return cnt

        if n % 2:
            n = (3 * n) + 1
        else:
            n = n/2


for n in range(1, 1000000):
    cycles[n] = cycle_of_length(n)

best_cycle = 0

for n in range(i, j):
    if cycles[n] > best_cycle:
        best_cycle = cycles[n]

print("{} {} {}".format(i, j, best_cycle))
