class Solution:
    @staticmethod
    def is_path_crossing(path: str) -> bool:
        directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        r, c = 0, 0
        v = {(0, 0)}
        for d in path:
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            if (nr, nc) in v:
                return True
            v.add((nr, nc))
            r, c = nr, nc
        return False
