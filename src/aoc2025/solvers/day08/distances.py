from collections import namedtuple
from math import sqrt


def calculate_distances(boxes):
    result = []
    for i in range(0, len(boxes)):
        for j in range(i + 1, len(boxes)):
            box_i = boxes[i]
            box_j = boxes[j]
            result.append(
                Distance(
                    {box_i.id, box_j.id},
                    _distance_between_points(box_i.coords, box_j.coords),
                )
            )
    return result


def _distance_between_points(point_a, point_b):
    num_dimensions = len(point_a)
    total = 0
    for i in range(0, num_dimensions):
        total += pow(point_a[i] - point_b[i], 2)
    return sqrt(total)


Distance = namedtuple("Distance", ["boxes", "value"])
