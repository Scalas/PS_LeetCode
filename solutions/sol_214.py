class Solution:
    @staticmethod
    def shortestPalindrome(s: str) -> str:
        n = len(s)
        rs = s[::-1]
        failure = [0] * n
        i, j = 1, 0
        while i + j < n:
            if s[i + j] == s[j]:
                j += 1
                failure[i + j - 1] = j
            else:
                if j == 0:
                    i += 1
                else:
                    i += j - failure[j - 1]
                    j = failure[j - 1]

        match = [0] * n
        i, j = 0, 0
        while i + j < n:
            if rs[i + j] == s[j]:
                j += 1
                match[i + j - 1] = j
            else:
                if j == 0:
                    i += 1
                else:
                    i += j - failure[j - 1]
                    j = failure[j - 1]
        return s[match[n - 1] :][::-1] + s
