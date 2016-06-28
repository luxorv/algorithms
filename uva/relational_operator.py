n = input().split()

t = n[0]

x = 1

while t:
    i = n[x]
    j = n[x+1]

    if i > j:
        print('>')
    if i < j:
        print('<')
    if i == j:
        print('=')
    x += 2
