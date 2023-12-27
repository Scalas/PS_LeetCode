from typing import List


class Solution:
    @staticmethod
    def min_cost(colors: str, neededTime: List[int]) -> int:
        pre = colors[0]
        cand = [neededTime[0]]
        answer = 0
        for i in range(1, len(colors)):
            c = colors[i]
            t = neededTime[i]
            if c == pre:
                cand.append(t)
            else:
                if len(cand) > 1:
                    cand.sort()
                    answer += sum(cand[:-1])
                pre, cand = c, [t]
        if len(cand) > 1:
            cand.sort()
            answer += sum(cand[:-1])
        return answer
