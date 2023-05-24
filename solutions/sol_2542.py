from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def max_score(nums1: List[int], nums2: List[int], k: int) -> int:
        q = []
        n = len(nums1)
        if n == 0:
            return 0

        for i in range(n):
            heappush(q, (-nums2[i], -nums1[i]))

        answer = 0
        s = []
        sumval = 0
        while q:
            bound = q[0][0]
            while q and q[0][0] == bound:
                num = -heappop(q)[1]
                if len(s) < k or num > s[0]:
                    heappush(s, num)
                    sumval += num
                    if len(s) > k:
                        sumval -= heappop(s)
            if len(s) == k:
                answer = max(answer, sumval * -bound)
        return answer
