n = int(input())

numbers = ['one', 'two', 'three']

for i in range(n):
    s = input()
    one = 'one'
    two = 'two'
    three = 'three'

    cnt1, cnt2, cnt3 = (0, 0, 0)

    for j in range(len(one)):
        if s[j] == one[j]:
            cnt1 += 1
        if s[j] == two[j]:
            cnt2 += 1
        if s[j] == three[j]:
            cnt3 += 1

    if cnt1 > cnt2:
        if cnt1 > cnt3:
            print(1)
        else:
            print(3)
    elif cnt2 > cnt1:
        if cnt2 > cnt3:
            print(2)
        else:
            print(3)
    elif cnt3 > cnt2:
        if cnt3 > cnt1:
            print(3)
        else:
            print(1)
