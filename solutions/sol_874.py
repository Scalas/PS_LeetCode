from typing import List


class Solution:
    @staticmethod
    def robot_sim(commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def rotate(cur, direction):
            if direction == -1:
                return (cur + 1) % 4
            if direction == -2:
                return (cur + 3) % 4
            return cur

        obstacles = set(map(tuple, obstacles))
        rr, rc, rd = 0, 0, 0
        answer = 0
        for cmd in commands:
            if cmd < 0:
                rd = rotate(rd, cmd)
            else:
                for _ in range(cmd):
                    dr, dc = directions[rd]
                    nr, nc = rr + dr, rc + dc
                    if (nr, nc) in obstacles:
                        break
                    rr, rc = nr, nc
                    answer = max(answer, rr**2 + rc**2)
        return answer
