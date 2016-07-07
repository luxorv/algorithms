t = int(input())

for i in range(t):

    speeds = list(map(int, input().split()))

    print("Case {}: {}".format(i+1, max(speeds)))
