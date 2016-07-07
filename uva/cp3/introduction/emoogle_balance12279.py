t = 0

while True:
    n = int(input())

    if n == 0:
        break

    events = list(map(int, input().split()))
    zeroes = events.count(0)
    reasons = len(events) - zeroes

    t += 1

    print("Case {}: {}".format(t, reasons - zeroes))
