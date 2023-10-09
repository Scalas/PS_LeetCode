from typing import List


class Solution:
    @staticmethod
    def search_range(nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        INF = 10**9 + 1
        nums.append(INF)
        s, e = 0, n
        while s < e:
            m = (s + e) // 2
            if nums[m] < target:
                s = m + 1
            else:
                e = m
        left = e if nums[e] == target else -1

        s, e = 0, n
        right = -1
        while s <= e:
            m = (s + e) // 2
            if nums[m] > target:
                e = m - 1
            else:
                right = m
                s = m + 1
        if nums[right] != target:
            right = -1

        return [left, right]
