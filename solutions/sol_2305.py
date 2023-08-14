from typing import List


class Solution:
    @staticmethod
    def distribute_cookies(cookies: List[int], k: int) -> int:
        n = len(cookies)
        answer = sum(sorted(cookies)[k - 1 :])

        def dfs(cur, bags):
            nonlocal answer
            if cur == n:
                answer = min(answer, max(bags))
                return
            for i in range(k):
                nsize = bags[i] + cookies[cur]
                if nsize >= answer:
                    continue
                back_up = bags[i]
                bags[i] = nsize
                dfs(cur + 1, bags)
                bags[i] = back_up

        dfs(0, [0] * k)
        return answer
