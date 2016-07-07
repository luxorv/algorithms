t = int(input())
:wq
:wq

for i in range(t):
    n = input()
    stores = list(map(int, input().split()))
    l = min(stores)
    r = max(stores)

    print(2 * (r - l))
