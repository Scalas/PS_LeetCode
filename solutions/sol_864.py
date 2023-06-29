from typing import List


class Solution:
    @staticmethod
    def shortest_path_all_keys(grid: List[str]) -> int:
        grid: List[List[str]] = [list(line) for line in grid]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        key_id = 0
        keys = dict()
        sr, sc = 0, 0
        for i in range(n):
            for j in range(m):
                c = grid[i][j]
                if c.islower():
                    keys[c] = key_id
                    key_id += 1
                elif c == '@':
                    sr, sc = i, j

        total_key = 2 ** (len(keys)) - 1
        visited = [[[False] * total_key for _ in range(m)] for _ in range(n)]
        q = [(sr, sc, 0)]
        answer = 0
        while q:
            answer += 1
            nq = []
            for cr, cc, key_state in q:
                for dr, dc in directions:
                    nr, nc, new_key_state = cr + dr, cc + dc, key_state
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    nxt = grid[nr][nc]
                    if nxt == '#':
                        continue
                    if nxt.islower():
                        new_key_state = key_state | (1 << keys[nxt])
                        if new_key_state == total_key:
                            return answer
                    elif nxt.isupper():
                        if not key_state & (1 << keys[nxt.lower()]):
                            continue
                    if visited[nr][nc][new_key_state]:
                        continue
                    visited[nr][nc][new_key_state] = True
                    nq.append((nr, nc, new_key_state))
            q = nq
        return -1
