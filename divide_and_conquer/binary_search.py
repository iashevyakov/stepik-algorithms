"""
https://stepik.org/lesson/13246/step/4?unit=3431
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if target == nums[middle]:
            return middle + 1  # в ответе необходима нумерация с 1
        if target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    n, *nums = list(map(int, input().split()))
    k, *targets = list(map(int, input().split()))
    indexes = [binary_search(nums, target) for target in targets]
    print(*indexes)