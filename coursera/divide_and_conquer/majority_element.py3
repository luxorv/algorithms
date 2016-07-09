import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = int(left + ((right - left)/2))

    lm = get_majority_element(a, left, mid)
    rm = get_majority_element(a, mid, right)

    cntl = 0
    cntr = 0

    for i in range(left, right):
        if a[i]== lm:
            cntl += 1
        elif a[i] == rm:
            cntr += 1

    half = mid - left

    if cntr >= half:
        return rm
    elif cntl >= half:
        return lm

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
