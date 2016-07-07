t = 0

while True:
    s = input()

    ans = ''

    if s == '#':
        break
    elif s == 'HELLO':
        ans = 'ENGLISH'
    elif s == 'HOLA':
        ans = 'SPANISH'
    elif s == 'BONJOUR':
        ans = 'FRENCH'
    elif s == 'HALLO':
        ans = 'GERMAN'
    elif s == 'CIAO':
        ans = 'ITALIAN'
    elif s == 'ZDRAVSTVUJTE':
        ans = 'RUSSIAN'
    else:
        ans = 'UNKNOWN'
    t += 1
    print("Case {}: {}".format(t, ans))
