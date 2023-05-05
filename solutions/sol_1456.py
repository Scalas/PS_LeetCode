class Solution:
    @staticmethod
    def max_vowels(s: str, k: int) -> int:
        vc = 0
        vowel = {'a', 'i', 'u', 'e', 'o'}
        for i in range(k):
            if s[i] in vowel:
                vc += 1

        answer = vc
        for i in range(len(s) - k):
            if s[i] in vowel:
                vc -= 1
            if s[k + i] in vowel:
                vc += 1
            answer = max(answer, vc)
        return answer
