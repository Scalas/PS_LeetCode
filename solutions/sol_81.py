from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> bool:
        n = len(nums)
        pre = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                pre = i

        s, e = 0, n - 1
        while s <= e:
            mid = (s + e) // 2
            num = nums[(mid + pre) % n]
            if num == target:
                return True
            if num < target:
                s = mid + 1
            else:
                e = mid - 1
        return False
