class Solution:
    @staticmethod
    def detect_capital_use(word: str) -> bool:
        boundary = ord('Z')
        word_case = list(map(lambda x: 0 if ord(x) > boundary else 1, word))
        case_sum = sum(word_case)
        if not case_sum:
            return True
        if case_sum == len(word):
            return True
        if case_sum == 1 and word_case[0] == 1:
            return True
        return False
