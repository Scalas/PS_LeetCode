from collections import deque


class Solution:
    @staticmethod
    def predict_party_victory(senate: str) -> str:
        n = len(senate)
        banned = [False] * n
        r = deque()
        d = deque()
        for i in range(n - 1, -1, -1):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        idx = -1
        while r or d:
            idx += 1
            if idx == n:
                idx = 0
            if banned[idx]:
                continue
            if senate[idx] == 'R':
                r.appendleft(r.pop())
                if d:
                    banned[d.pop()] = True
                if not d:
                    return 'Radiant'
            else:
                d.appendleft(d.pop())
                if r:
                    banned[r.pop()] = True
                if not r:
                    return 'Dire'
