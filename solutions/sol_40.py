from typing import List


class Solution:
    @staticmethod
    def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
        n = target + 1
        count = [0] * n
        for num in candidates:
            if num > target:
                continue
            count[num] += 1

        def dfs(cur, remain):
            nonlocal comb, answer
            if remain == 0:
                res = []
                for x in range(len(comb)):
                    if comb[x] == 0:
                        continue
                    res.extend([x] * comb[x])
                answer.append(res)
            if cur == n:
                return
            if cur > remain:
                return
            for i in range(count[cur] + 1):
                comb.append(i)
                dfs(cur + 1, remain - cur * i)
                comb.pop()

        comb = [0]
        answer = []
        dfs(1, target)
        return answer
