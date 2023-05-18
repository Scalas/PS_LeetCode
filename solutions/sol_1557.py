from typing import List, Set


class Solution:
    @staticmethod
    def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> Set[int]:
        return set(range(n)) - set([v for _, v in edges])
