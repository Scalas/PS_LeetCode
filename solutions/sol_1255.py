from typing import List


class Solution:
    @staticmethod
    def max_score_words(words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        max_counts = [0] * 26
        for c in letters:
            max_counts[ord(c) - ord("a")] += 1

        alpha_counts = [[0] * 26 for _ in range(n)]
        for i in range(n):
            word = words[i]
            for c in word:
                alpha_counts[i][ord(c) - ord("a")] += 1

        def dfs(cur, cnt):
            nonlocal n, answer
            if cur == n:
                res = 0
                for i in range(26):
                    if cnt[i] > max_counts[i]:
                        return
                    res += score[i] * cnt[i]
                answer = max(answer, res)
                return
            word = words[cur]
            org = cnt[:]
            for c in word:
                cnt[ord(c) - ord("a")] += 1
            dfs(cur + 1, cnt)
            cnt = org
            dfs(cur + 1, cnt)

        answer = 0
        dfs(0, [0] * 26)
        return answer
