def euclidian_gcd(a, b):
    if b == 0:
        return a

    ap = a % b

    return euclidian_gcd(b, ap)


def lcm(a, b):
    gcd = euclidian_gcd(a, b)
    mult = a * b

    return mult//gcd


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
