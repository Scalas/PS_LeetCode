from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_content_children(g: List[int], s: List[int]) -> int:
        count = defaultdict(int)
        for size in s:
            count[size] += 1
        q = sorted(map(list, count.items()))[::-1]
        answer = 0
        g.sort()
        for ms in g:
            while q and q[-1][0] < ms:
                q.pop()
            if not q:
                break
            q[-1][1] -= 1
            if q[-1][1] == 0:
                q.pop()
            answer += 1
        return answer
