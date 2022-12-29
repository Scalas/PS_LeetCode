from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def get_order(tasks: List[List[int]]) -> List[int]:
        task_at = []
        n = len(tasks)
        for i in range(n):
            heappush(task_at, (tasks[i][0], tasks[i][1], i))

        answer = []
        q = []
        time = 0
        while len(answer) < n:
            while task_at and task_at[0][0] <= time:
                _, proc_time, task_index = heappop(task_at)
                heappush(q, (proc_time, task_index))
            if q:
                proc_time, task_index = heappop(q)
                answer.append(task_index)
                time += proc_time
            elif task_at:
                time = max(time, task_at[0][0])

        return answer
