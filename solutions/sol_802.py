from typing import List


class Solution:
    @staticmethod
    def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
        graph = list(map(lambda x: set(x), graph))
        n = len(graph)
        reverse_graph = [set() for _ in range(n)]
        for i in range(n):
            for nxt in graph[i]:
                reverse_graph[nxt].add(i)

        q = [i for i in range(n) if not graph[i]]
        answer = []
        while q:
            nq = []
            for cur in q:
                answer.append(cur)
                for pre in reverse_graph[cur]:
                    graph[pre].remove(cur)
                    if not graph[pre]:
                        nq.append(pre)
            q = nq
        answer.sort()
        return answer
