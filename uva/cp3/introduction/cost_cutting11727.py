t = int(input())

for i in range(t):
    salaries = sorted(list(map(int, input().split())))
    print("Case {}: {}".format(i+1, salaries[1]))
