from typing import List

ALPHA_COUNT = 26


class Solution:
    @staticmethod
    def count_sub_trees(n: int, edges: List[List[int]], labels: str) -> List[int]:
        labels = list(map(lambda x: ord(x) - ord('a'), labels))
        label_count = [[0] * ALPHA_COUNT for _ in range(n)]
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        answer = [0] * n

        def dfs(cur):
            label = labels[cur]
            label_count[cur][label] = 1
            for nxt in g[cur]:
                nxt_label = labels[nxt]
                if label_count[nxt][nxt_label]:
                    continue
                dfs(nxt)
                for i in range(ALPHA_COUNT):
                    label_count[cur][i] += label_count[nxt][i]
            answer[cur] = label_count[cur][label]

        dfs(0)

        return answer
