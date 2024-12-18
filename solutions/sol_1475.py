from typing import List


class Solution:
    @staticmethod
    def final_prices(prices: List[int]) -> List[int]:
        n = len(prices)
        res = []
        for i in range(n):
            p = prices[i]
            for j in range(i + 1, n):
                if prices[j] <= p:
                    p -= prices[j]
                    break
            res.append(p)
        return res
