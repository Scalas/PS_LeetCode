from typing import List


class Solution:
    @staticmethod
    def largest_altitude(gain: List[int]) -> int:
        answer = 0
        acc = 0
        for num in gain:
            acc += num
            answer = max(answer, acc)
        return answer
