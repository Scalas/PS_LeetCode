class Solution:
    @staticmethod
    def remove_duplicate_letters(s: str) -> str:
        n = len(s)
        s = list(map(lambda x: ord(x) - ord("a"), s))

        indexes = [[] for _ in range(26)]
        for i in range(n):
            indexes[s[i]].append(i)
        for i in range(26):
            indexes[i] = indexes[i][::-1]

        remain = [0] * n
        remain[-1] = 1 << s[-1]
        for i in range(n - 2, -1, -1):
            remain[i] = remain[i + 1] | (1 << s[i])

        mask = 0
        aset = set(s)
        for c in aset:
            mask |= 1 << c

        answer = []
        padding = ord("a")
        visited = [False] * 26
        last = 0
        for _ in range(len(aset)):
            for i in range(26):
                while indexes[i] and indexes[i][-1] < last:
                    indexes[i].pop()
                if not indexes[i]:
                    continue
                if visited[i]:
                    continue
                idx = indexes[i][-1]
                if mask & remain[idx] == mask:
                    answer.append(chr(i + padding))
                    indexes[i].pop()
                    mask -= 1 << i
                    visited[i] = True
                    last = idx
                    break

        return "".join(answer)
