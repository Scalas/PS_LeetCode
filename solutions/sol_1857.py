from typing import List


class Solution:
    @staticmethod
    def largest_path_value(colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        nexts = [set() for _ in range(n)]
        prevs = [set() for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            nexts[u].add(v)
            prevs[v].add(u)
        starts = [i for i in range(n) if not prevs[i]]

        deleted = [False] * n
        q = [i for i in range(n) if not nexts[i] or not prevs[i]]
        dc = 0
        for target in q:
            deleted[target] = True
        while q:
            nq = []
            dc += len(q)
            for target in q:
                for nxt in nexts[target]:
                    prevs[nxt].remove(target)
                    if not prevs[nxt] and not deleted[nxt]:
                        deleted[nxt] = True
                        nq.append(nxt)
                for prev in prevs[target]:
                    nexts[prev].remove(target)
                    if not nexts[prev] and not deleted[prev]:
                        deleted[prev] = True
                        nq.append(prev)
            q = nq
        if dc < n:
            return -1

        colors = list(map(lambda x: ord(x) - ord('a'), colors))

        # dp[i][j] 는 i번 노드로부터 시작하는 모든 경로의 j 색상의 빈도중 최댓값
        dp = [[-1] * 26 for _ in range(n)]

        def dfs(cur, color):
            if dp[cur][color] < 0:
                mv = 0
                for nxt in g[cur]:
                    mv = max(mv, dfs(nxt, color))
                dp[cur][color] = mv + (1 if colors[cur] == color else 0)
            return dp[cur][color]

        answer = 0
        for color in set(colors):
            for start in starts:
                answer = max(answer, dfs(start, color))
        return answer
