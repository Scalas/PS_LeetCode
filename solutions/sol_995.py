from typing import List


class Solution:
    @staticmethod
    def min_k_bit_flips(nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = [0] * (n + 1)
        answer = 0
        for i in range(n):
            if i > 0:
                flipped[i] = (flipped[i] + flipped[i - 1]) % 2
            num = nums[i]
            if flipped[i]:
                num = 1 - num
            if num == 0:
                if i + k > n:
                    return -1
                answer += 1
                flipped[i] += 1
                flipped[i + k] -= 1
        return answer
