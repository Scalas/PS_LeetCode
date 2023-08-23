class Solution:
    @staticmethod
    def reorganize_string(s: str) -> str:
        n = len(s)
        answer = []
        count = [0] * 26
        visit = [-2] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for i in range(n):
            cnt, alpha = 0, 0
            for j in range(26):
                if visit[j] == i - 1:
                    continue
                if count[j] > cnt:
                    cnt, alpha = count[j], j
            if cnt == 0:
                return ""
            visit[alpha] = i
            count[alpha] -= 1
            answer.append(chr(ord('a') + alpha))
        return "".join(map(str, answer))
