from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def group_the_people(group_sizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        for i in range(len(group_sizes)):
            size = group_sizes[i]
            if group[size] and len(group[size][-1]) < size:
                group[size][-1].append(i)
            else:
                group[size].append([i])

        answer = []
        for g in group.values():
            answer.extend(g)
        return answer
