from typing import List


class Solution:
    @staticmethod
    def min_operations(logs: List[str]) -> int:
        answer = 0
        for log in logs:
            if log == "../":
                if answer > 0:
                    answer -= 1
                continue
            if log == "./":
                continue
            answer += 1
        return answer
