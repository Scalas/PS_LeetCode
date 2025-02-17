from collections import defaultdict


class Solution:
    @staticmethod
    def num_tile_possibilities(tiles: str) -> int:
        fact = [0, 1, 2, 6, 24, 120, 720, 5040]
        cnt = defaultdict(int)
        for c in tiles:
            cnt[c] += 1

        values = list(cnt.values())
        n = len(values)
        buf = []
        answer = 0

        def dfs(cur):
            nonlocal n, buf, values, answer
            if cur == n:
                if buf:
                    res = fact[sum(buf)]
                    if res == 0:
                        return
                    for x in buf:
                        if x == 0:
                            continue
                        res //= fact[x]
                    answer += res
                    return
            for i in range(values[cur] + 1):
                buf.append(i)
                dfs(cur + 1)
                buf.pop()

        dfs(0)
        return answer
