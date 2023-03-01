from typing import List


class Solution:
    @staticmethod
    def sort_array(nums: List[int]) -> List[int]:
        count = [0] * 100001
        c = 50000
        for num in nums:
            count[num + c] += 1

        answer = []
        for i in range(100001):
            while count[i]:
                answer.append(i - c)
                count[i] -= 1
        return answer
