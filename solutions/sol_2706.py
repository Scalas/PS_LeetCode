from typing import List


class Solution:
    @staticmethod
    def buy_choco(prices: List[int], money: int) -> int:
        if len(prices) < 2:
            return money
        prices.sort()
        p = prices[0] + prices[1]
        return money - p if p <= money else money
