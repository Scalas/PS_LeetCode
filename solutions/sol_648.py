from typing import List


class Solution:
    @staticmethod
    def replace_words(dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        dictionary.sort(key=lambda x: len(x))
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
        return " ".join(words)
