from typing import List


class Solution:
    @staticmethod
    def find_kth_positive(arr: List[int], k: int) -> int:
        last = 0
        for num in arr:
            missing = num - last - 1
            if missing < k:
                k -= missing
                last = num
            else:
                return last + k
        return last + k
