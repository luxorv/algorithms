from random import randint

def euclidian_gcd(a, b):
    if b == 0:
        return a

    ap = a % b

    return euclidian_gcd(b, ap)

def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def test():

    while True:
        a = randint(1, 3234)
        b = randint(1, 423)

        naive = gcd(a, b)
        euc = euclidian_gcd(a, b)

        if naive != euc:
            print("Wrong Answer: naive {} - euc {}".format(naive, euc))
        else:
            print("Ok a {} b {} - gcd {}".format(a, b, euc))

if __name__ == "__main__":
    test()

    # input = sys.stdin.read()
    # a, b = map(int, input.split())
