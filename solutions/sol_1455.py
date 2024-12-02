class Solution:
    @staticmethod
    def is_prefix_of_word(sentence: str, searchWord: str) -> int:
        tokens = sentence.split(" ")
        for i in range(len(tokens)):
            if tokens[i].startswith(searchWord):
                return i + 1
        return -1
