n = input().split()

l = []

print(n)

for i in range(len(n)):
    mx = max(n)
    l.append(mx)
    n.remove(mx)

print(l)
