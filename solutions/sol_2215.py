from typing import List


class Solution:
    @staticmethod
    def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ns1 = set(nums1)
        ns2 = set(nums2)
        return [sorted(ns1 - ns2), sorted(ns2 - ns1)]
