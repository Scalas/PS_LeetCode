from typing import List


class Solution:
    @staticmethod
    def min_patches(nums: List[int], n: int) -> int:
        nums.append(10**10)
        cur = 0
        last = 1
        answer = 0
        while last <= n:
            num = nums[cur]
            if num <= last:
                last += num
                cur += 1
            else:
                answer += 1
                last *= 2
        return answer
