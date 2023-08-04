from typing import List


class Solution:
    @staticmethod
    def word_break(s: str, word_dict: List[str]) -> bool:
        n = len(s)
        g = [[] for _ in range(n)]
        for word in word_dict:
            for i in range(n):
                if s[i] != word[0]:
                    continue
                if s[i:i+len(word)] == word:
                    g[i].append(i + len(word))

        q = [0]
        visited = [False] * n
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if nxt == n:
                        return True
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
        return False
