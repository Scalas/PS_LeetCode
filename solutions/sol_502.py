from typing import List
from heapq import heappush, heappop


class Solution:
    @staticmethod
    def find_maximized_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted([(capital[i], profits[i]) for i in range(n)], reverse=True)
        q = []
        current_capital = w
        for _ in range(k):
            while projects and projects[-1][0] <= current_capital:
                heappush(q, -(projects.pop()[1]))
            if not q:
                break
            current_capital -= heappop(q)
        return current_capital
