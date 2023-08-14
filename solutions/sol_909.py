from typing import List


class Solution:
    @staticmethod
    def snakes_and_ladders(board: List[List[int]]) -> int:
        n = len(board)
        node_num = n**2
        g = [-1] * (node_num + 1)
        for i in range(n):
            start = (n - i) * n
            if i % 2 != n % 2:
                start -= n - 1
            step = 1 if i % 2 != n % 2 else -1
            for j in range(n):
                cur = start + j * step
                nxt = board[i][j]
                if nxt != -1:
                    g[cur] = nxt

        q = [1]
        count = 0
        visited = [False] * (node_num + 1)
        visited[1] = True
        while q:
            nq = []
            for cur in q:
                if cur == node_num:
                    return count
                max_nxt = min(cur + 6, node_num)
                for nxt in range(cur + 1, max_nxt + 1):
                    if g[nxt] == -1:
                        continue
                    nxt = g[nxt]
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
                for nxt in range(max_nxt, cur, -1):
                    if not visited[nxt] and g[nxt] == -1:
                        visited[nxt] = True
                        nq.append(nxt)
                        break
            count += 1
            q = nq

        return -1
