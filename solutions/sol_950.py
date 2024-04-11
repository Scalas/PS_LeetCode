from math import ceil
from collections import deque
from typing import List


class Solution:
    @staticmethod
    def deck_revealed_increasing(deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        half = ceil(n / 2)

        res = [0] * n
        for i in range(half):
            res[i * 2] = deck[i]

        remain = deck[half:]
        indexes = deque(range(1, n, 2))
        if n % 2 and remain:
            indexes.append(indexes.popleft())
        for num in remain:
            idx = indexes.popleft()
            if indexes:
                indexes.append(indexes.popleft())
            res[idx] = num
        return res
