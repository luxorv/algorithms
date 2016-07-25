t = int(input())

while t > 0:

    n, m, s = map(int, input().split())
    ans = int(((n/m) + s) * m)
    print(ans)

    t -= 1
