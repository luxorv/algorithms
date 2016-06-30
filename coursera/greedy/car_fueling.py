n = open('input', 'r').read().split()

full_tank = int(n[0])
paths = list(map(int, n[1:]))
destination = int(n[-1])


def naive_car_fuel():
    refills = 0
    cur_tank = full_tank

    for index in range(len(paths) - 1):
        distance_to_next_station = abs(paths[index+1] - paths[index])
        cur_tank -= distance_to_next_station

        if cur_tank < distance_to_next_station:
            cur_tank = full_tank
            refills += 1

    print(refills)


def min_car_fuel(paths, full_tank, destination):
    cur_refill, refill_cnt = (0, 0)

    while cur_refill <= destination:
        last_refill = cur_refill

        while cur_refill <= destination and paths[cur_refill+1] - paths[last_refill] <= full_tank:
            cur_refill += 1

        if cur_refill == last_refill:
            return -1

        if refill_cnt <= destination:
            refill_cnt += 1

    return refill_cnt


print(min_car_fuel(paths, full_tank, len(paths)-2))
