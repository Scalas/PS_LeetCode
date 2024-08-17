from typing import List


class Solution:
    @staticmethod
    def lemonade_change(bills: List[int]) -> bool:
        cur = {5: 0, 10: 0, 20: 0}
        for b in bills:
            cur[b] += 1
            change = b - 5
            if change == 0:
                continue
            if change == 5:
                if cur[5] == 0:
                    return False
                cur[5] -= 1
            else:
                if cur[10] > 0 and cur[5] > 0:
                    cur[10] -= 1
                    cur[5] -= 1
                    continue
                if cur[5] > 2:
                    cur[5] -= 3
                    continue
                return False
        return True
