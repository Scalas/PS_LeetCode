from typing import List


class Solution:
    @staticmethod
    def num_of_minutes(
        n: int, head_id: int, manager: List[int], inform_time: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for i in range(n):
            if i == head_id:
                continue
            g[manager[i]].append(i)

        q = [(head_id, 0)]
        answer = 0
        while q:
            nq = []
            for cur, time in q:
                if not g[cur]:
                    answer = max(answer, time)
                    continue
                for nxt in g[cur]:
                    nq.append((nxt, time + inform_time[cur]))
            if nq:
                q = nq
            else:
                break
        return answer
