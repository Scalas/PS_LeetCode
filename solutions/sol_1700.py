from typing import List


class Solution:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        pre = -1
        sandwiches = sandwiches[::-1]
        while students:
            if pre == len(students):
                return len(students)
            pre = len(students)
            nq = []
            for cur in students:
                if sandwiches[-1] == cur:
                    sandwiches.pop()
                else:
                    nq.append(cur)
            if not nq:
                return 0
            students = nq
