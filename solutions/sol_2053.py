from typing import List


class Solution:
    @staticmethod
    def kth_distinct(arr: List[str], k: int) -> str:
        idx = 0
        index = dict()
        count = dict()
        for c in arr:
            index[c] = idx
            count[c] = count.get(c, 0) + 1
            idx += 1
        a = sorted([c for c in arr if count[c] == 1], key=lambda x: index[x])
        k = min(len(a), k - 1)
        a.append("")
        return a[k]
