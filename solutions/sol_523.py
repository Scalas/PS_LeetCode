from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def check_subarray_sum(nums: List[int], k: int) -> bool:
        n = len(nums)
        nums[0] %= k
        for i in range(n - 1):
            nums[i + 1] = (nums[i + 1] + nums[i]) % k
        count = defaultdict(int)
        pre = 0
        for num in nums:
            if count[num] > 0:
                return True
            count[pre] += 1
            pre = num
        return False
