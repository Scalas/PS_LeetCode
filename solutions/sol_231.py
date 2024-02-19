class Solution:
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2:
                return False
            n //= 2
        return True
