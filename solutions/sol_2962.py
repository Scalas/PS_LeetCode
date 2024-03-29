from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def count_sub_arrays(nums: List[int], k: int) -> int:
        n = len(nums)
        nums.append(0)
        count = defaultdict(int)
        e = 0
        mv = max(nums)
        answer = 0
        for s in range(n):
            count[nums[s - 1]] -= 1
            if count[mv] == k:
                answer += n - e + 1
                continue
            while e < n and count[mv] < k:
                count[nums[e]] += 1
                e += 1
                if count[mv] >= k:
                    answer += n - e + 1
                    break
        return answer
