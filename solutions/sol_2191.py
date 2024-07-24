from typing import List


class Solution:
    @staticmethod
    def sort_jumbled(mapping: List[int], nums: List[int]) -> List[int]:
        basis = dict()
        for i in range(len(nums)):
            num = nums[i]
            conv = int("".join(map(lambda x: str(mapping[int(x)]), str(num))))
            basis[num] = (conv, i)
        return sorted(nums, key=lambda x: basis[x])
