import sys

def binary_search(a, left, right, x):

    if right < left:
        return -1

    mid = int(left + ((right - left)/2))

    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, left, mid-1, x)
    elif x > a[mid]:
        return binary_search(a, mid+1, right, x)

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
        index = binary_search(a, 0, len(a) - 1, x)
        if index == None:
            index = -1
        print(index, end = ' ')
