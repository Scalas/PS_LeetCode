from typing import List


class Solution:
    @staticmethod
    def max_ice_cream(costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        answer = 0
        while coins and costs:
            if coins >= costs[-1]:
                coins -= costs.pop()
                answer += 1
            else:
                break
        return answer
