class Solution:
    @staticmethod
    def total_money(n: int) -> int:
        r = n // 7
        rem = n % 7
        base = 28
        answer = 0

        cnt = 0
        for _ in range(r):
            answer += base + cnt * 7
            cnt += 1
        answer += ((1 + rem) * rem // 2) + cnt * rem
        return answer
