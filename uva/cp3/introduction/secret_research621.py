n = int(input())

for i in range(n):

    s = input()

    if s == '4' or s == '78':
        print('+')
    elif s[-2:] == '35':
        print('-')
    elif s[0] == '9' and s[-1] == '4':
        print('*')
    elif s[:3] == '190':
        print('?')
