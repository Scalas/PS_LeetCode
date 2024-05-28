class Solution:
    @staticmethod
    def equal_substring(s: str, t: str, max_cost: int) -> int:
        n = len(s)
        diff = [abs(ord(t[i]) - ord(s[i])) for i in range(n)]
        q = []
        s = 0
        total = 0
        answer = 0
        for d in diff:
            q.append(d)
            total += d
            while total > max_cost:
                total -= q[s]
                s += 1
            answer = max(answer, len(q) - s)
        return answer
