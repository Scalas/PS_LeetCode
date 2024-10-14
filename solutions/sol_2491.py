from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def divide_players(skill: List[int]) -> int:
        half = len(skill) // 2
        total = sum(skill)
        if total % half:
            return -1

        count: dict[int, int] = defaultdict(int)
        for s in skill:
            count[s] += 1

        answer = 0
        target = total // half
        for s in skill:
            if count[s] == 0:
                continue
            count[s] -= 1
            p = target - s
            if count[p] > 0:
                answer += s * p
                count[p] -= 1
            else:
                return -1
        return answer
