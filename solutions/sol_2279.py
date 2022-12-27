from heapq import heappush, heappop
from typing import List


class Solution:
    @staticmethod
    def maximum_bags(capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
        empty_bags = []
        answer = 0
        for i in range(len(capacity)):
            if capacity[i] == rocks[i]:
                answer += 1
            else:
                heappush(empty_bags, capacity[i] - rocks[i])
        while additional_rocks and empty_bags:
            bag = heappop(empty_bags)
            if additional_rocks >= bag:
                answer += 1
                additional_rocks -= bag
            else:
                break
        return answer
