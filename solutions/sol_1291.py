from typing import List


class Solution:
    @staticmethod
    def sequential_digits(low: int, high: int) -> List[int]:
        s, e = len(str(low)), len(str(high))
        answer = []
        for d in range(s, e + 1):
            u = int("".join(map(str, range(1, d + 1))))
            g = int("1" * d)
            while u % 10:
                if u > high:
                    break
                if u >= low:
                    answer.append(u)
                u += g
        return answer
