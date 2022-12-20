from typing import List


class Solution:
    @staticmethod
    def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        q = [0]
        visited = [False] * len(rooms)
        visited[0] = True
        count = 1
        while q:
            nq = []
            for cur in q:
                for nxt in rooms[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    count += 1
                    nq.append(nxt)
            q = nq
        return count == len(rooms)
