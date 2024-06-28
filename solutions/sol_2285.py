from typing import List


class Solution:
    @staticmethod
    def maximum_importance(n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        for u, v in roads:
            count[u] += 1
            count[v] += 1
        nodes = [-1] * n
        value = n
        for node in sorted(range(n), key=lambda x: -count[x]):
            nodes[node] = value
            value -= 1

        answer = 0
        for u, v in roads:
            answer += nodes[u] + nodes[v]
        return answer
