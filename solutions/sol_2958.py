from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def max_sub_array_length(nums: List[int], k: int) -> int:
        count = defaultdict(int)
        s, e = 0, 0
        n = len(nums)
        answer = 0
        while e < n:
            num = nums[e]
            count[num] += 1
            if count[num] > k:
                answer = max(answer, e - s)
            e += 1
            while s < e and count[num] > k:
                count[nums[s]] -= 1
                s += 1
        answer = max(answer, e - s)
        return answer
