from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def find_least_num_of_unique_ints(arr: List[int], k: int) -> int:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        count = sorted(map(list, count.items()), key=lambda x: -x[1])
        while count and count[-1][1] <= k:
            k -= count.pop()[1]
        return len(count)
