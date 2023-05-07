from typing import List
from bisect import bisect_right


class Solution:
    @staticmethod
    def longest_obstacle_course_at_each_position(obstacles: List[int]) -> List[int]:
        lis = []
        answer = []
        for num in obstacles:
            if not lis or lis[-1] <= num:
                lis.append(num)
                answer.append(len(lis))
            else:
                idx = bisect_right(lis, num)
                lis[idx] = num
                answer.append(idx + 1)
        return answer
