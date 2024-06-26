from typing import List


class Solution:
    @staticmethod
    def number_of_sub_arrays(nums: List[int], k: int) -> int:
        n = len(nums)
        odds = []
        for i in range(n):
            if nums[i] % 2:
                odds.append(i)

        m = len(odds)
        answer = 0
        for i in range(m - k + 1):
            pre = odds[i]
            if i > 0:
                pre -= odds[i - 1]
            else:
                pre += 1
            nxt = -odds[i + k - 1]
            if i + k < m:
                nxt += odds[i + k]
            else:
                nxt += n
            answer += pre * nxt
        return answer
