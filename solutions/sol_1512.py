from typing import List


class Solution:
    @staticmethod
    def num_identical_pairs(nums: List[int]) -> int:
        counter = dict()
        answer = 0
        for num in nums[::-1]:
            pre = counter.get(num, 0)
            answer += pre
            counter[num] = pre + 1
        return answer
