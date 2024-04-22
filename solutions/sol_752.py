from typing import List


class Solution:
    @staticmethod
    def open_lock(dead_ends: List[str], target: str) -> int:
        dead_ends = set(dead_ends)
        if target == "0000":
            return 0
        if "0000" in dead_ends:
            return -1

        def wrap(num):
            if num < 0:
                return 9
            if num > 9:
                return 0
            return num

        q = [[0, 0, 0, 0]]
        visited = set()
        op = [
            [1, 0, 0, 0],
            [-1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, -1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, -1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, -1],
        ]
        depth = 0
        while q:
            depth += 1
            nq = []
            for u, v, w, x in q:
                for ou, ov, ow, ox in op:
                    nu, nv, nw, nx = map(wrap, [u + ou, v + ov, w + ow, x + ox])
                    key = "".join(map(str, [nu, nv, nw, nx]))
                    if key == target:
                        return depth
                    if key in dead_ends:
                        continue
                    if key in visited:
                        continue
                    visited.add(key)
                    nq.append([nu, nv, nw, nx])
            q = nq
        return -1
