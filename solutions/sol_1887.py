from typing import List


class Solution:
    @staticmethod
    def reduction_operations(nums: List[int]) -> int:
        mv = max(nums)
        ncount = [0] * (mv + 1)
        for num in nums:
            ncount[num] += 1

        answer = 0
        pre = 0
        for i in range(mv + 1):
            if not ncount[i]:
                continue
            answer += ncount[i] * pre
            pre += 1
        return answer
