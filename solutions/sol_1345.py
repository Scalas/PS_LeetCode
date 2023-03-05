from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def min_jumps(arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        group = defaultdict(list)
        for i in range(n):
            num = arr[i]
            group[num].append(i)

        q = [0]
        visited = [False] * n
        visited[0] = True
        group_visited = defaultdict(bool)
        jump = 0
        while q:
            jump += 1
            nq = []
            for cur in q:
                if cur > 0:
                    nxt = cur - 1
                    if nxt == n - 1:
                        return jump
                    if not visited[nxt]:
                        visited[nxt] = True
                        nq.append(nxt)
                if cur < n - 1:
                    nxt = cur + 1
                    if nxt == n - 1:
                        return jump
                    if not visited[nxt]:
                        visited[nxt] = True
                        nq.append(nxt)
                group_id = arr[cur]
                if group_visited[group_id]:
                    continue
                group_visited[group_id] = True
                for nxt in group[group_id]:
                    if nxt == n - 1:
                        return jump
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
        return -1
