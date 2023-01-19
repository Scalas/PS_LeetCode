from typing import List


class Solution:
    @staticmethod
    def sub_arrays_div_by_k(nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * k
        basis = 0
        answer = 0
        for num in nums:
            r = num % k
            basis = (basis + k - r) % k
            dp[(basis + r) % k] += 1
            answer += dp[basis]
        return answer
