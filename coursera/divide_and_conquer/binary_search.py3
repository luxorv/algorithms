import sys

def binary_search(a, x):
    left, right = 0, len(a)

    if right < left:
        return -1

    mid = int(left + (right - left)/2)

    if a[mid] == x:
        return mid

    if x < a[mid]:
        return binary_search(a[left:mid-1], x)
    elif a[mid] > x:
        return binary_search(a[mid+1:right], x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        index = binary_search(a, x)
        if index == None:
            index = -1
        print(index, end = ' ')
