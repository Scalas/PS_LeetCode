from collections import defaultdict
from heapq import heappop, heapify
from typing import List


class Solution:
    @staticmethod
    def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
        count = defaultdict(int)
        heapify(hand)
        for num in hand:
            count[num] += 1
        idx = 0
        while hand:
            idx += 1
            while hand and count[hand[0]] == 0:
                heappop(hand)
            if not hand:
                break
            start = heappop(hand)
            count[start] -= 1
            for i in range(start + 1, start + group_size):
                if count[i] == 0:
                    return False
                count[i] -= 1
        return True
