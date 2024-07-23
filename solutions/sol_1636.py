from typing import List


class Solution:
    @staticmethod
    def frequency_sort(nums: List[int]) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        return sorted(nums, key=lambda x: (frequency[x], -x))
