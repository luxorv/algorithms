import sys

input = sys.stdin

n = ''

for line in sys.stdin:
    n += line

cnt = 1
new_s = ''

for i in n:
    c = i
    if i is '"' and cnt % 2 is not 0:
        cnt += 1
        # print("{} ~> ``".format(i))
        new_s += '``'
    elif i is '"' and cnt % 2 is 0:
        cnt += 1
        # print("{} ~> ''".format(i))
        new_s += "''"
    else:
        new_s += c

print(new_s, end='')
