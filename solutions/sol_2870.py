from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def min_operations(nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        answer = 0
        for cnt in count.values():
            removed = False
            for i in range(cnt // 2 + 1):
                remain = cnt - 2 * i
                if remain % 3:
                    continue
                removed = True
                answer += i + remain // 3
                break
            if not removed:
                return -1
        return answer
