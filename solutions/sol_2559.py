from typing import List


class Solution:
    @staticmethod
    def vowel_strings(words: List[str], queries: List[List[int]]) -> List[int]:
        vs = {"a", "i", "u", "e", "o"}
        n = len(words)
        acc = [0] * n
        for i in range(n):
            word = words[i]
            if word[0] in vs and word[-1] in vs:
                acc[i] += 1
            if i > 0:
                acc[i] += acc[i - 1]
        acc.append(0)
        answer = []
        for u, v in queries:
            answer.append(acc[v] - acc[u - 1])
        return answer
