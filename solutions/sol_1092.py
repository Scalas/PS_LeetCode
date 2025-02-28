class Solution:
    @staticmethod
    def shortest_common_super_sequence(str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[-1] * m for _ in range(n)]
        trace = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                mv = 0
                direction = -1
                if i > 0:
                    match = dp[i - 1][j]
                    if match > mv:
                        mv, direction = match, 1  # up
                if j > 0:
                    match = dp[i][j - 1]
                    if match > mv:
                        mv, direction = match, 2  # left
                if str1[i] == str2[j]:
                    if i > 0 and j > 0:
                        match = dp[i - 1][j - 1] + 1
                        if match > mv:
                            mv, direction = match, 0  # diag
                    else:
                        match = 1
                        if match > mv:
                            mv, direction = match, -1
                dp[i][j] = mv
                trace[i][j] = direction
        sr, sc = n - 1, m - 1
        path = []
        while True:
            if trace[sr][sc] == 0:
                path.append([sr, sc])
                sr, sc = sr - 1, sc - 1
            elif trace[sr][sc] == 1:
                sr, sc = sr - 1, sc
            elif trace[sr][sc] == 2:
                sr, sc = sr, sc - 1
            else:
                if str1[sr] == str2[sc]:
                    path.append([sr, sc])
                break
        i1 = list(range(n))[::-1]
        i2 = list(range(m))[::-1]
        buf = []
        for u, v in path[::-1]:
            while i1 and i1[-1] < u:
                buf.append(str1[i1.pop()])
            if i1:
                i1.pop()
            while i2 and i2[-1] < v:
                buf.append(str2[i2.pop()])
            if i2:
                i2.pop()
            buf.append(str1[u])
        while i1:
            buf.append(str1[i1.pop()])
        while i2:
            buf.append(str2[i2.pop()])
        return "".join(buf)
