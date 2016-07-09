import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key=lambda s: s.end)
    points = set()
    right_most = segments[0].end

    for s in segments:
        if right_most >= s.start and right_most <= s.end:
            points.add(right_most)
        else:
            right_most = s.end
            points.add(right_most)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
