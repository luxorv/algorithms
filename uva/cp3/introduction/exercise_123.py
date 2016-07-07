def read_double():
    '''Read in a double, echo it, but with a minimum length field of 7 and 3
    digits after the decimal point eg. 1.4732 ~> ss1.473 and
    15.324547327 ~> s15.325
    '''
    n = input()
    lst = n.split('.')
    print('s' * (3 - len(lst[0])) + lst[0] + '.' + lst[1][:3])


def pi():
    '''Read a N and outputs N digits of Pi N <= 15'''
    n = int(input())
    for k in range(n):
        p = (1/16) * ((4/((8 * k) + 4)) - (2/((8 * k) + 4)) - (1/((8 * k) + 5))- (1/((8 * k) + 6)))
        print(round(p, 3))


def week_day():
    '''Read date like 9 August 2010 and outputs the day number'''
    from datetime import datetime
    n = input()
    print(datetime.strptime(n, '%d %B %Y').weekday())


def n_random():
    n = sorted([ int(i) for i in input().split()])
    x = {i for i in n}
    print(x)
