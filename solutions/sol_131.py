from typing import List


class Solution:
    @staticmethod
    def partition(s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
        for g in range(2, n):
            for i in range(n - g):
                j = i + g
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]

        answer = []
        palindrome = []

        def dfs(cur, start):
            if cur == n:
                if start == n:
                    answer.append(palindrome[:])
                return
            if is_palindrome[start][cur]:
                palindrome.append(s[start:cur + 1])
                dfs(cur + 1, cur + 1)
                palindrome.pop()
            dfs(cur + 1, start)

        dfs(0, 0)

        return answer
