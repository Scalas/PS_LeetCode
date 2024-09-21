from typing import List


class Solution:
    @staticmethod
    def lexical_order(n: int) -> List[int]:
        answer = []
        maxv = n
        cand = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        count = 0

        def dfs(cur):
            nonlocal answer, count
            if int(cur) > maxv:
                return False
            answer.append(int(cur))
            count -= 1
            if count == 0:
                return False
            for c in cand:
                if not dfs(cur + c):
                    break
            return True

        for c in cand[1:]:
            if not dfs(c):
                break
        return answer
