import sys

from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def fast_count_segments(segments, points):
    cnt = [0] * len(points)
    segments = sorted(segments, key=lambda s: s.end)

    for i in range(len(points)):
        for j in range(len(segments)):
            if segments[j].start > points[i]:
                break
            if segments[j].start <= points[i] <= segments[j].end:
                cnt[i] += 1
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))

    n = data[0]
    m = data[1]

    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(starts, ends)))
    cnt = fast_count_segments(segments, points)

    for x in cnt:
        print(x, end=' ')
