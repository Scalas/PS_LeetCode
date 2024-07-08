from collections import deque


class Solution:
    @staticmethod
    def find_the_winner(n: int, k: int) -> int:
        q = deque([i for i in range(1, n + 1)])
        idx = 0
        while len(q) > 1:
            idx += 1
            cur = q.popleft()
            if idx % k:
                q.append(cur)
        return q[0]
