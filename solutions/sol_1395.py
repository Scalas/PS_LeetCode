from typing import List


class Solution:
    @staticmethod
    def num_teams(rating: List[int]) -> int:
        answer = 0
        n = len(rating)
        for i in range(1, n -1):
            lgc, llc = 0, 0
            for j in range(i):
                if rating[j] > rating[i]:
                    lgc += 1
                else:
                    llc += 1
            rgc, rlc = 0, 0
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    rgc += 1
                else:
                    rlc += 1
            answer += lgc * rlc + llc * rgc
        return answer
