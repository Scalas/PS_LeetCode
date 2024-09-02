from typing import List


class Solution:
    @staticmethod
    def chalk_replacer(chalk: List[int], k: int) -> int:
        t = sum(chalk)
        k %= t
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
