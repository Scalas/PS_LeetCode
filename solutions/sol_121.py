from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        answer = 0
        for i in range(1, len(prices)):
            answer = max(answer, prices[i] - prices[i - 1])
            prices[i] = min(prices[i], prices[i - 1])
        return answer
