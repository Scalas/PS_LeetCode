from typing import List, Tuple


class Solution:
    @staticmethod
    def find_number_of_lis(nums: List[int]) -> int:
        n = len(nums)
        minus = 10**6
        nums = list(map(lambda x: x + minus, nums))

        def dfs(cur, last) -> Tuple[int, int]:
            if cur == n:
                return 0, 1
            if dp[cur].get(last, -1) == -1:
                length, count = dfs(cur + 1, last)
                if nums[cur] > last:
                    nl, nc = dfs(cur + 1, nums[cur])
                    nl += 1
                    if nl > length:
                        length, count = nl, nc
                    elif nl == length:
                        count += nc
                dp[cur][last] = length, count
            return dp[cur][last]

        dp = [dict() for _ in range(n)]
        return dfs(0, 0)[1]
