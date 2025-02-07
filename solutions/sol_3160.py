from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def query_results(_limit: int, queries: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        color = defaultdict(int)
        cc = 0
        answer = []
        for u, v in queries:
            org = color[u]
            if org in count:
                count[org] -= 1
                if count[org] == 0:
                    cc -= 1
            color[u] = v
            if count[v] == 0:
                cc += 1
            count[v] += 1
            answer.append(cc)
        print(color)
        return answer
