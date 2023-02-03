from typing import List


class Solution:
    @staticmethod
    def four_sum(nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        answer = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                two_sum = target - nums[i] - nums[j]
                count = {nums[n - 1]}
                for k in range(n - 2, j, -1):
                    t = two_sum - nums[k]
                    if t in count:
                        answer.add(tuple(sorted((nums[i], nums[j], nums[k], t))))
                    count.add(nums[k])
        return list(map(list, answer))
