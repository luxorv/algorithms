t = int(input())

money = 0

for i in range(t):

    query = input()

    if query[0] == 'r':
        print(money)
    else:
        money += int(query.split()[1])
