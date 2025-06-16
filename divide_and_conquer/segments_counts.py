"""
https://stepik.org/lesson/13249/step/6?unit=3434
"""
from bisect import bisect_right, bisect_left
from typing import List


def segments_cnt_for_points(points: List[int]) -> List[int]:
    segments_cnt = []
    for point in points:
        n = bisect_right(left_points, point)
        m = bisect_left(right_points, point)
        segments_cnt.append(n - m)
    return segments_cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    points = list(map(int, input().split()))
    left_points = [segment[0] for segment in segments]
    right_points = [segment[1] for segment in segments]
    left_points.sort()
    right_points.sort()
    segments_cnt = segments_cnt_for_points(points)
    print(*segments_cnt)