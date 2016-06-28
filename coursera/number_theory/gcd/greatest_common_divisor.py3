def euclidian_gcd(a, b):
    if b == 0:
        return a

    ap = a % b

    return euclidian_gcd(b, ap)

a, b = map(int, input().split())

print(euclidian_gcd(a, b))
