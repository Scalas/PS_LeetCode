class Solution:
    @staticmethod
    def integer_break(n: int) -> int:
        answer = n - 1
        for i in range(2, n):
            c = n // i - 1
            if not c:
                continue
            m1 = (i**c) * (i + n % i)
            m2 = (i ** (c + 1)) * (n % i)
            answer = max(answer, m1, m2)
        return answer
