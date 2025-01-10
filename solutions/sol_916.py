from typing import List


class Solution:
    @staticmethod
    def word_subsets(words1: List[str], words2: List[str]) -> List[str]:
        universal = [0] * 26
        base = ord("a")
        for word in words2:
            count = [0] * 26
            for c in word:
                count[ord(c) - base] += 1
            for i in range(26):
                universal[i] = max(universal[i], count[i])

        answer = []
        for word in words1:
            count = [0] * 26
            for c in word:
                count[ord(c) - base] += 1
            is_universal = True
            for i in range(26):
                if universal[i] > count[i]:
                    is_universal = False
                    break
            if is_universal:
                answer.append(word)
        return answer
