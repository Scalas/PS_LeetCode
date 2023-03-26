from typing import List


class Solution:
    @staticmethod
    def longest_cycle(edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n

        def search_cycle(cur):
            visit_idx = dict()
            idx = 0
            while cur != -1 and cur not in visit_idx:
                if visited[cur]:
                    return -1
                visited[cur] = True
                visit_idx[cur] = idx
                idx += 1
                cur = edges[cur]

            if cur == -1:
                return -1
            return idx - visit_idx[cur]

        answer = -1
        for i in range(n):
            if not visited[i]:
                answer = max(answer, search_cycle(i))
        return answer
