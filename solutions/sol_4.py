from typing import List


class Solution:
    @staticmethod
    def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
        s = []
        l = len(nums1) + len(nums2)
        while nums1 and nums2:
            if nums1[-1] > nums2[-1]:
                s.append(nums1.pop())
            else:
                s.append(nums2.pop())

        if nums1:
            s.extend(nums1[::-1])
        if nums2:
            s.extend(nums2[::-1])

        h = l // 2
        if l % 2:
            return s[h]
        else:
            return (s[h - 1] + s[h]) / 2
