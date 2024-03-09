from typing import List


class Solution:
    @staticmethod
    def get_common(nums1: List[int], nums2: List[int]) -> int:
        try:
            return min(set(nums1) & set(nums2))
        except ValueError:
            return -1
