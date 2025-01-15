class Solution:
    @staticmethod
    def minimize_xor(num1: int, num2: int) -> int:
        answer = num1
        bc1, bc2 = 0, 0
        while num1:
            bc1 += num1 % 2
            num1 //= 2
        while num2:
            bc2 += num2 % 2
            num2 //= 2

        if bc1 == bc2:
            return answer

        if bc1 > bc2:
            bit = 1
            for _ in range(bc1 - bc2):
                while answer & bit == 0:
                    bit <<= 1
                answer -= bit
            return answer

        if bc1 < bc2:
            bit = 1
            for _ in range(bc2 - bc1):
                while answer & bit > 0:
                    bit <<= 1
                answer += bit

        return answer
