class Solution:
    @staticmethod
    def get_happy_string(n: int, k: int) -> str:
        idx = 0
        s = ["a", "b", "c"]
        buf = []

        def dfs(cur):
            nonlocal s, buf, idx

            if cur == n:
                idx += 1
                return idx == k
            for c in s:
                if buf and buf[-1] == c:
                    continue
                buf.append(c)
                if dfs(cur + 1):
                    return True
                buf.pop()
            return False

        dfs(0)
        return "".join(buf)
