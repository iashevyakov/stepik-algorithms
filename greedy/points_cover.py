"""
https://stepik.org/lesson/13238/step/9?unit=3424
"""
def points_for_covering(segments):
    # сортировка отрезков по возрастанию правой границы
    sorted_segments = sorted(segments, key=lambda s: s[1])
    i = 0
    points = []
    while i < n:
        # берем правую границу очередного отрезка
        r = sorted_segments[i][1]
        while i < n and sorted_segments[i][0] <= r:
            i += 1
        points.append(r)  # добавляем точку в ответ
    return points


if __name__ == "__main__":
    n = int(input())
    segments = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]

    points = points_for_covering(segments)
    print(len(points))
    print(*points)