import sys

for line in sys.stdin.readlines():
    start, first_number, second_number, third_number = map(int, line.split())


    if start is 0 and first_number is 0 and second_number is 0 and third_number is 0:
        break

    angles = 0

    conter1 = 40 - first_number + start
    wise1 = start - first_number

    angles += conter1 if first_number > start else wise1

    conter2 = 40 - first_number + second_number
    wise2 = second_number - first_number

    angles += wise2 if second_number > first_number else conter2

    conter3 =  40 + second_number - third_number
    wise3 = second_number - third_number

    angles += conter3 if third_number > second_number else wise3

    angles *= 9
    angles += 1080

    print(angles)
