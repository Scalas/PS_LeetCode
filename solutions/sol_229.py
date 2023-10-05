from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def majority_element(nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        basis = len(nums) // 3
        answer = []
        for i, c in count.items():
            if c > basis:
                answer.append(i)
        return answer
