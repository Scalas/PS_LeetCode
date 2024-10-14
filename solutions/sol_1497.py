from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def can_arrange(arr: List[int], k: int) -> bool:
        count: dict[int, int] = defaultdict(int)
        for num in arr:
            count[num % k] += 1
        if count[0] % 2:
            return False
        for i in range(1, k // 2 + 1):
            if count[i] != count[k - i]:
                return False
        return True
