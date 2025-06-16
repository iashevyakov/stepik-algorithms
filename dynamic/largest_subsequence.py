"""
https://stepik.org/lesson/13257/step/5
"""

from typing import List


def largest_subsequence_len(nums: List[int]) -> int:
    d = []
    for i in range(len(nums)):
        d.append(1)
        for j in range(i):
            if nums[i] % nums[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    ls_len = largest_subsequence_len(nums)
    print(ls_len)