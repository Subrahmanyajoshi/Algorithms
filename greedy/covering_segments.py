# Uses python3
import sys
from collections import namedtuple

import numpy as np

Segment = namedtuple('Segment', 'start end')


def common(list1, list2):
    common_elements = list(set(list1).intersection(list2))
    return common_elements


def optimal_points(s):
    segments = []
    for i in s:
        segments.append(np.arange(i.start, i.end + 1).tolist())

    segments.sort()
    points = []

    merge_points = []
    for i in range(1, len(segments)):
        c_elements = common(segments[i - 1], segments[i])
        if len(merge_points) == 0:
            merge_points = c_elements
            continue
        merge_common = common(merge_points, c_elements)
        if len(merge_common) == 0:
            points.append(merge_points[-1])
            merge_points = []
            continue
        merge_points = merge_common
    if merge_points:
        points.append(merge_points[-1])
    return points


if __name__ == '__main__':
    # segments = [[1, 3], [2, 5], [3, 6]]
    # segments = [[4, 7], [1, 3], [2, 5], [5, 6]]

    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
