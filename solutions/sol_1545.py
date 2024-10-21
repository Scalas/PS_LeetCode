class Solution:
    @staticmethod
    def find_kth_bit(n: int, k: int) -> str:
        s = [0]
        for _ in range(n - 1):
            s.append(1)
            for i in range(len(s) - 2, -1, -1):
                s.append(1 - s[i])
        return str(s[k - 1])
