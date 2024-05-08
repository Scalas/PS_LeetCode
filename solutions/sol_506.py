from typing import List


class Solution:
    @staticmethod
    def find_relative_ranks(score: List[int]) -> List[str]:
        def get_rank(idx):
            if idx == 0:
                return "Gold Medal"
            if idx == 1:
                return "Silver Medal"
            if idx == 2:
                return "Bronze Medal"
            return str(idx + 1)

        n = len(score)
        indexed_score = [[score[i], i] for i in range(n)]
        indexed_score.sort(reverse=True)
        res = [""] * n
        for i in range(n):
            _, idx = indexed_score[i]
            res[idx] = get_rank(i)
        return res
