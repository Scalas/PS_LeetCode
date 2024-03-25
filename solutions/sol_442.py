from typing import List


class Solution:
    @staticmethod
    def find_duplicates(nums: List[int]) -> List[int]:
        s = set()
        res = []
        while nums:
            num = nums.pop()
            if num in s:
                s.remove(num)
                res.append(num)
            else:
                s.add(num)
        return res
