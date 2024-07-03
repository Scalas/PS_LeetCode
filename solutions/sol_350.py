from collections import defaultdict
from typing import List, Dict


class Solution:
    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        count: Dict[int] = defaultdict(int)
        for num in nums1:
            count[num] += 1
        answer = []
        for num in nums2:
            if count[num] > 0:
                count[num] -= 1
                answer.append(num)
        return answer
