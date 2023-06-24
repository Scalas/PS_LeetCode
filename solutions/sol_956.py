from typing import List


class Solution:
    @staticmethod
    def tallest_billboard(rods: List[int]) -> int:
        half = len(rods) // 2
        r1, r2 = rods[:half], rods[half:]
        left, right = {0: (0, 0)}, {0: (0, 0)}

        def dfs(cur, first, second):
            if cur == n:
                if first > second:
                    first, second = second, first
                diff = second - first
                pairs[diff] = max(pairs.get(diff, (-1, -1)), (first, second))
                return
            dfs(cur + 1, first, second)
            dfs(cur + 1, first + rods[cur], second)
            dfs(cur + 1, first, second + rods[cur])

        n = len(r1)
        rods = r1
        pairs = left
        dfs(0, 0, 0)

        n = len(r2)
        rods = r2
        pairs = right
        dfs(0, 0, 0)

        answer = 0
        for diff, pair in left.items():
            left1, left2 = pair
            if diff not in right:
                continue
            right1, right2 = right[diff]
            answer = max(answer, left1 + right2)

        return answer
