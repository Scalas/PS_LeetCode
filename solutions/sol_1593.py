class Solution:
    @staticmethod
    def max_unique_split(s: str) -> int:
        answer = 0
        n = len(s)

        def check(ends):
            if not ends:
                return True
            subset = set()
            for i in range(1, len(ends)):
                u, v = ends[i - 1] + 1, ends[i] + 1
                substring = s[u:v]
                if substring in subset:
                    return False
                subset.add(substring)
            return True

        def dfs(cur, ends):
            nonlocal answer

            if cur == n:
                if check(ends):
                    answer = max(answer, len(ends) - 1)
                return

            ends.append(cur)
            dfs(cur + 1, ends)
            ends.pop()
            dfs(cur + 1, ends)

        dfs(0, [-1])
        return answer
