from typing import List


class Solution:
    @staticmethod
    def max_count(banned: List[int], n: int, max_sum: int) -> int:
        candidates = sorted(set(range(1, n + 1)) - set(banned))
        s = 0
        answer = 0
        for num in candidates:
            s += num
            if s > max_sum:
                break
            answer += 1
        return answer
