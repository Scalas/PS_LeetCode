class Solution:
    @staticmethod
    def is_power_of_four(n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1
