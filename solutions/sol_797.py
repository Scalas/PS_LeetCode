from typing import List


class Solution:
    @staticmethod
    def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
        answer = []
        n = len(graph)

        def dfs(path):
            if path[-1] == n - 1:
                answer.append(path[:])

            for nxt in graph[path[-1]]:
                path.append(nxt)
                dfs(path)
                path.pop()

        dfs([0])

        return answer

