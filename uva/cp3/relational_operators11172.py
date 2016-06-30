n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    sign = ['>', '<', '=']

    if a > b:
        print(sign[0])
    elif a < b:
        print(sign[1])
    else:
        print(sign[2])
