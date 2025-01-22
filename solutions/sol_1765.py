from typing import List


class Solution:
    @staticmethod
    def highest_peak(is_water: List[List[int]]) -> List[List[int]]:
        q = []
        n, m = len(is_water), len(is_water[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        answer = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if is_water[i][j] == 1:
                    q.append([i, j])
                    answer[i][j] = 0
        height = 0
        while q:
            height += 1
            nq = []
            for cu, cv in q:
                for dr, dc in directions:
                    nu, nv = cu + dr, cv + dc
                    if not (0 <= nu < n and 0 <= nv < m):
                        continue
                    if answer[nu][nv] != -1:
                        continue
                    answer[nu][nv] = height
                    nq.append([nu, nv])
            q = nq
        return answer
