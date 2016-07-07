t = int(input())

for i in range(t):
    ans = 'bad'

    length, width, height = map(int, input().split())

    if length <= 20 and width <= 20 and height <= 20:
        ans = 'good'

    print("Case {}: {}".format(i+1, ans))
