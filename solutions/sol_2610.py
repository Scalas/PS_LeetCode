from typing import List


class Solution:
    @staticmethod
    def find_matrix(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        count = [0] * (n + 1)
        answer = []
        for num in nums:
            if count[num] == len(answer):
                answer.append([])
            answer[count[num]].append(num)
            count[num] += 1
        return answer
