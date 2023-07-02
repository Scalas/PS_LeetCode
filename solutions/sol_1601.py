from typing import List


class Solution:
    @staticmethod
    def maximum_requests(n: int, requests: List[List[int]]) -> int:
        edges = [pair for pair in requests if pair[0] != pair[1]]
        fixed = len(requests) - len(edges)
        answer = 0
        in_out = [[0, 0] for _ in range(n)]

        def dfs(cur, cnt):
            nonlocal answer
            if cur == len(edges):
                check = True
                for i in range(len(in_out)):
                    if in_out[i][0] != in_out[i][1]:
                        check = False
                        break
                if check:
                    answer = max(answer, cnt)
                return
            dfs(cur + 1, cnt)
            u, v = edges[cur]
            in_out[u][1] += 1
            in_out[v][0] += 1
            dfs(cur + 1, cnt + 1)
            in_out[u][1] -= 1
            in_out[v][0] -= 1

        dfs(0, 0)
        return answer + fixed
