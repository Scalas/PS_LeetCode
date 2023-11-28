class Solution:
    @staticmethod
    def number_of_ways(corridor: str) -> int:
        n = len(corridor)
        ranges = []
        scnt = 0
        start = -1
        for i in range(n):
            if corridor[i] == "S":
                scnt += 1
                if scnt % 2 and start != -1:
                    ranges.append([start, i])
                else:
                    start = i
        if scnt == 0 or scnt % 2:
            return 0
        answer = 1
        mod = 10**9 + 7
        for u, v in ranges:
            answer = (answer * (v - u)) % mod

        return answer % mod
