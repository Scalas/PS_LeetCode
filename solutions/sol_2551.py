from typing import List


class Solution:
    @staticmethod
    def put_marbles(weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        cand = [weights[i] + weights[i - 1] for i in range(1, len(weights))]
        cand.sort()
        return sum(cand[1 - k:]) - sum(cand[:k - 1])
