from typing import List


class Solution:
    @staticmethod
    def find_all_concatenated_words_in_a_dict(words: List[str]) -> List[str]:
        word_set = set(words)
        answer = set()

        def dfs(w, start):
            if start == len(w):
                answer.add(w)
                return
            for end in range(start, len(w)):
                part = w[start:end + 1]
                if part in word_set:
                    dfs(w, end + 1)

        for word in words:
            word_set.remove(word)
            dfs(word, 0)
            word_set.add(word)
        return list(answer)
