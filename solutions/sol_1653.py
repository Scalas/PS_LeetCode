class Solution:
    @staticmethod
    def minimum_deletions(s: str) -> int:
        left, right = [0, 0], [0, 0]
        ms = [0 if c == "a" else 1 for c in s]
        for i in ms:
            right[i] += 1
        answer = 10 ** 6
        for i in ms:
            right[i] -= 1
            answer = min(answer, left[1] + right[0])
            left[i] += 1
        return answer
