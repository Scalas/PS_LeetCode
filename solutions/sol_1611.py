class Solution:
    @staticmethod
    def minimum_one_bit_operations(n: int) -> int:
        if n == 0:
            return 0

        binary = []
        while n:
            binary.append(n % 2)
            n //= 2
        dp = [0] * len(binary)
        dp[0] = 1
        for i in range(1, len(binary)):
            dp[i] = dp[i - 1] * 2 + 1

        sign = 1
        answer = 0
        for i in range(len(binary) - 1, -1, -1):
            if binary[i]:
                answer += dp[i] * sign
                sign *= -1
        return answer
