from typing import List


class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = dict()


class Solution:
    @staticmethod
    def longest_common_prefix(arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))

        tri = dict()

        def insert(s: str):
            cur = tri
            for c in s:
                if c not in cur:
                    cur[c] = Node(c)
                cur = cur[c].next

        def count(s: str):
            cur = tri
            res = 0
            for c in s:
                if c in cur:
                    res += 1
                    cur = cur[c].next
                else:
                    break
            return res

        for num in arr1:
            insert(num)

        return max([count(num) for num in arr2])
