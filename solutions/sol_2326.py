from typing import Optional, List

from leet_code_types.leet_code_types import ListNode


class Solution:
    @staticmethod
    def spiral_matrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        board = [[-1] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cr, cc, cd = 0, 0, 0

        def get_next(cur_row, cur_column, cur_direction):
            dr, dc = directions[cur_direction]
            nr, nc, nd = cur_row + dr, cur_column + dc, cur_direction
            if not (0 <= nr < m and 0 <= nc < n) or board[nr][nc] != -1:
                nd = (nd + 1) % 4
                dr, dc = directions[nd]
                nr, nc = cur_row + dr, cur_column + dc
            return nr, nc, nd

        cursor = head
        while cursor:
            board[cr][cc] = cursor.val
            cr, cc, cd = get_next(cr, cc, cd)
            cursor = cursor.next
        return board
