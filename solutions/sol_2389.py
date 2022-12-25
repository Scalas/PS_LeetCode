from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def answer_queries(nums: List[int], queries: List[int]) -> List[int]:
        answers = []
        for query in queries:
            answer = 0
            q = []
            sum_val = 0
            for num in nums:
                sum_val += num
                heappush(q, -num)
                while sum_val > query:
                    sum_val += heappop(q)
                answer = max(answer, len(q))
            answers.append(answer)
        return answers
