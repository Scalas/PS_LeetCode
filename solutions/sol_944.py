from typing import List


class Solution:
    @staticmethod
    def min_deletion_size(strs: List[str]) -> int:
        answer = 0
        for column in zip(*strs):
            pre = 'a'
            for c in column:
                if c < pre:
                    answer += 1
                    break
                else:
                    pre = c
        return answer
