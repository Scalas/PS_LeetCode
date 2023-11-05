from typing import List
from collections import deque


class Solution:
    @staticmethod
    def get_winner(arr: List[int], k: int) -> int:
        mv = max(arr)
        q = deque(arr)
        cand = q.popleft()
        win = 0
        while True:
            if win == k:
                return cand
            if cand == mv:
                return cand
            while cand > q[0]:
                win += 1
                if win == k:
                    return cand
                q.append(q.popleft())
            q.append(cand)
            cand, win = q.popleft(), 1
