from typing import List


class Solution:
    @staticmethod
    def time_required_to_buy(tickets: List[int], k: int) -> int:
        c = tickets[k]
        answer = c
        for i in range(k):
            answer += min(c, tickets[i])
        for i in range(k + 1, len(tickets)):
            answer += min(c - 1, tickets[i])
        return answer
