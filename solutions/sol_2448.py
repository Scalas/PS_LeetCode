from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def min_cost(nums: List[int], cost: List[int]) -> int:
        m, total, cur_cost = min(nums), sum(cost), 0
        acc = defaultdict(int)
        for num, cost in zip(nums, cost):
            acc[num] += cost
            cur_cost += (num - m) * cost

        nums = sorted(acc.keys())
        n = len(nums)
        answer = cur_cost
        for i in range(1, n):
            acc[nums[i]] += acc[nums[i - 1]]

        for i in range(1, n):
            num, pre = nums[i], nums[i - 1]
            g = num - pre
            cur_cost += (acc[nums[i - 1]] * 2 - total) * g
            answer = min(answer, cur_cost)
        return answer
