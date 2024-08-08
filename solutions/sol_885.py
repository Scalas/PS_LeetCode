from typing import List


class Solution:
    @staticmethod
    def spiral_matrix_3(
        rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        answer = []
        r, c = rStart, cStart
        answer.append([r, c])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d, w, cnt = 0, 1, 1
        total = rows * cols

        while cnt < total:
            for _ in range(w):
                dr, dc = directions[d]
                r += dr
                c += dc
                if not (0 <= r < rows and 0 <= c < cols):
                    continue
                cnt += 1
                answer.append([r, c])

            d = (d + 1) % 4
            for _ in range(w):
                dr, dc = directions[d]
                r += dr
                c += dc
                if not (0 <= r < rows and 0 <= c < cols):
                    continue
                cnt += 1
                answer.append([r, c])

            d = (d + 1) % 4
            w += 1
            for _ in range(w):
                dr, dc = directions[d]
                r += dr
                c += dc
                if not (0 <= r < rows and 0 <= c < cols):
                    continue
                cnt += 1
                answer.append([r, c])

            d = (d + 1) % 4
            for _ in range(w):
                dr, dc = directions[d]
                r += dr
                c += dc
                if not (0 <= r < rows and 0 <= c < cols):
                    continue
                cnt += 1
                answer.append([r, c])
            d = (d + 1) % 4
            w += 1
        return answer
