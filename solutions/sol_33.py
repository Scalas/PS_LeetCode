from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                pivot = i
                break

        s, e = 0, n - 1
        while s <= e:
            mid = (s + e) // 2
            idx = (mid + pivot) % n
            check = nums[idx] - target
            if check == 0:
                return idx
            if check < 0:
                s = mid + 1
            else:
                e = mid - 1
        return -1
