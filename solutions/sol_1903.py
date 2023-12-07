class Solution:
    @staticmethod
    def largest_odd_number(num: str) -> str:
        n = len(num)
        end = -1
        for i in range(n - 1, -1, -1):
            d = int(num[i])
            if d % 2:
                end = i
                return num[: i + 1]
        return ""
