from typing import List


class Solution:
    @staticmethod
    def num_sub_array_product_less_than_k(nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        product = 1
        answer = 0
        for e in range(n):
            product *= nums[e]
            while s < e and product >= k:
                product //= nums[s]
                s += 1
            if product < k:
                answer += e - s + 1
        return answer
