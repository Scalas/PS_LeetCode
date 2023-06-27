from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        index = [0] * n
        q = [[nums1[i] + nums2[0], i, 0] for i in range(n)]
        heapify(q)
        answer = []
        while q and len(answer) < k:
            s, x, y = heappop(q)
            answer.append([nums1[x], nums2[y]])
            if y + 1 < m:
                heappush(q, [nums1[x] + nums2[y + 1], x, y + 1])
                index[x] += 1
        return answer
