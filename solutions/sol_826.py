from heapq import heapify, heappop
from typing import List


class Solution:
    @staticmethod
    def max_profit_assignment(
        difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        tasks = [[-profit[i], difficulty[i]] for i in range(len(difficulty))]
        heapify(tasks)
        workers = sorted(worker, reverse=True)

        answer = 0
        for p in workers:
            while tasks and tasks[0][1] > p:
                heappop(tasks)
            if not tasks:
                break
            answer -= tasks[0][0]
        return answer
