from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def total_fruit(fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        count = 0
        type_count = 0
        begin = 0
        answer = 0
        for f in fruits:
            if fruit_count[f] == 0:
                type_count += 1
            while type_count > 2:
                pop_fruit = fruits[begin]
                fruit_count[pop_fruit] -= 1
                if fruit_count[pop_fruit] == 0:
                    type_count -= 1
                count -= 1
                begin += 1

            fruit_count[f] += 1
            count += 1
            answer = max(answer, count)
        return answer
