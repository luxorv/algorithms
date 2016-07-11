import sys


def get_number_of_inversions(a):

    if len(a) <= 1:
        return 0, a

    mid = len(a) // 2

    rb, b = get_number_of_inversions(a[:mid])
    rc, c = get_number_of_inversions(a[mid:])

    d = []
    rbc = 0

    while len(b) and len(c):

        if b[0] <= c[0]:
            d.append(b.pop(0))
        else:
            d.append(c.pop(0))
            rbc += len(b)

    d += b + c

    return (rb + rc + rbc), d


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a)[0])
