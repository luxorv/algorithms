import sys

input = sys.stdin

def read_from_std():

    for line in sys.stdin:
        yield line

def read_from_file():

    def rotate(num, counter_clockwise=False):
        num = 39. if num == 0 else float(num)

        if counter_clockwise:
            return 360./(40./(40. - num))
        else:
            return 360./(40./num)

    n = open('input', 'r').read().strip().split('\n')
    combinations = [[float(j) for j in i.split()] for i in n]

    for line in combinations:
        start = line[0]
        first_number = line[1]
        second_number = line[2]
        third_number = line[3]

        angles = 360.* 2.
        angles += rotate(first_number) - rotate(start, counter_clockwise=True)
        angles += 360.
        angles += rotate(second_number, counter_clockwise=True)
        angles += rotate(third_number)

        print(angles - rotate(start))

read_from_file()
