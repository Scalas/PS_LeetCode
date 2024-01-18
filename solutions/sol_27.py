from typing import List


class Solution:
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i] != val:
                res.append(nums[i])
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)
