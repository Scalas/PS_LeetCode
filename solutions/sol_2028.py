from typing import List


class Solution:
    @staticmethod
    def missing_rolls(rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        need = mean * (m + n) - sum(rolls)
        if need > 6 * n:
            return []
        if need < n:
            return []
        answer = [need // n] * n
        for i in range(need % n):
            answer[i] += 1
        return answer
