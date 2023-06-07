class Solution:
    @staticmethod
    def min_flips(a: int, b: int, c: int) -> int:
        answer = 0
        while a | b | c:
            target = c % 2
            cur_a = a % 2
            cur_b = b % 2
            if cur_a | cur_b != target:
                if target == 0:
                    answer += (cur_a + cur_b)
                else:
                    answer += 1
            c //= 2
            a //= 2
            b //= 2
        return answer
