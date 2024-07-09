from typing import List


class Solution:
    @staticmethod
    def average_waiting_time(customers: List[List[int]]) -> float:
        cur = 0
        answer = 0
        for u, v in customers:
            arrived = u
            response = max(cur, u) + v
            answer += response - arrived
            cur = response
        return answer / len(customers)
