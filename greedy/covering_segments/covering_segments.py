from collections import namedtuple
import sys
import numpy as np

Segment = namedtuple('Segment', 'start end')


class CoveringSegments(object):

    @staticmethod
    def common(list1, list2):
        common_elements = list(set(list1).intersection(list2))
        return common_elements

    @staticmethod
    def optimal_points(s):
        segments = []
        for i in s:
            if i.start == i.end:
                segments.append([i.start, i.end])
                continue
            segments.append(np.arange(i.start, i.end + 1).tolist())

        segments.sort()
        points = []

        merge_points = segments[0]
        for i in range(1, len(segments)):
            c_elements = CoveringSegments.common(segments[i - 1], segments[i])
            merge_common = CoveringSegments.common(merge_points, c_elements)

            if len(merge_common) == 0:
                points.append(merge_points[-1])
                merge_points = segments[i]
                continue
            merge_points = merge_common

        if merge_points:
            points.append(merge_points[-1])
        return points


if __name__ == '__main__':
    regions = [[1, 3], [2, 5], [3, 6]]
    # regions = [[4, 7], [1, 3], [2, 5], [5, 6]]
    # regions = [[1, 1], [1, 3], [1, 2], [4, 4], [0, 1], [3, 4], [2, 4], [5, 5], [7, 8], [2, 4], [8, 8]]
    # regions = [[2, 4], [5, 5], [7, 8]]
    segments = []
    #
    for segment in regions:
        segments.append(Segment(segment[0], segment[1]))
    # input = sys.stdin.read()
    # n, *data = map(int, input.split())
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = CoveringSegments.optimal_points(segments)
    print(len(points))
    print(*points)
