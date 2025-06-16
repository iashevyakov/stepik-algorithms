"""
https://stepik.org/lesson/13252/step/3?unit=3437
"""
from typing import List


def count_sort(n: int, nums: List[int]) -> List[int]:
    max_num, min_num = max(nums), min(nums)
    m = (max_num - min_num + 1)
    counts = [0] * m
    for num in nums:
        counts[num - min_num] += 1
    for i in range(1, m):
        counts[i] = counts[i - 1] + counts[i]
    sorted_nums = [0] * n
    for j in range(n - 1, -1, -1):  # для обеспечения "стабильности" сортировки
        sorted_nums[counts[nums[j] - min_num] - 1] = nums[j]
        counts[nums[j] - min_num] -= 1
    return sorted_nums


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = count_sort(n, nums)
    print(*sorted_nums)
