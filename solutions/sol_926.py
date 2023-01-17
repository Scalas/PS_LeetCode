class Solution:
    @staticmethod
    def min_flips_mono_increasing(s: str) -> int:
        n = len(s)
        count = [0] * (n + 1)
        for i in range(n):
            count[i] = int(s[i])
            if i > 0:
                count[i] += count[i - 1]

        answer = min(count[n - 1], n - count[n - 1])
        for i in range(n):
            answer = min(answer, count[i - 1] + (n - i - count[n - 1] + count[i - 1]))
        return answer
