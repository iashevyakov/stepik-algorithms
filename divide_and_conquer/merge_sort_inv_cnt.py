"""
https://stepik.org/lesson/13248/step/5?unit=3433
"""
from typing import List, Tuple


def merge(nums_1: List[int], nums_2: List[int]) -> Tuple[List[int], int]:
    merged = []
    i, j = 0, 0
    inv_cnt = 0
    while i < len(nums_1) and j < len(nums_2):
        if nums_1[i] <= nums_2[j]:
            merged.append(nums_1[i])
            i += 1
        else:
            merged.append(nums_2[j])
            j += 1
            inv_cnt += len(nums_1) - i
    for k in range(i, len(nums_1)):
        merged.append(nums_1[k])
    for k in range(j, len(nums_2)):
        merged.append(nums_2[k])
    return merged, inv_cnt


def merge_sort(nums: List[int]) -> Tuple[List[int], int]:
    if len(nums) == 1:
        return nums, 0
    mid = len(nums) // 2

    left, inv_left = merge_sort(nums[0: mid])
    right, inv_right = merge_sort(nums[mid: len(nums)])
    merged_nums, inv_merge = merge(left, right)
    return merged_nums, inv_left + inv_right + inv_merge


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    _, inv_cnt = merge_sort(nums)
    print(inv_cnt)