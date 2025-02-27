from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def len_longest_fib_subseq(arr: List[int]) -> int:
        n = len(arr)
        dp = [defaultdict(int) for _ in range(n)]
        answer = 0
        for i in range(n):
            num = arr[i]
            for j in range(i):
                pre = arr[j]
                pp = num - pre
                if pp == pre or pp not in dp[j]:
                    dp[i][pre] = 2
                else:
                    dp[i][pre] = dp[j][pp] + 1
                    answer = max(answer, dp[i][pre])
        return answer
