from typing import List


class Solution:
    @staticmethod
    def single_non_duplicate(nums: List[int]) -> int:
        st = set()
        for num in nums:
            if num in st:
                st.remove(num)
            else:
                st.add(num)
        for num in st:
            return num
