class Solution:
    @staticmethod
    def find_complement(num: int) -> int:
        binary = []
        while num:
            binary.append(1 - num % 2)
            num //= 2
        return int("".join(map(str, binary[::-1])), 2)
