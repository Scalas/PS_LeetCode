from typing import List


class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = dict()
        self.count = 0


class Solution:
    @staticmethod
    def sum_prefix_scores(words: List[str]) -> List[int]:
        tri = dict()

        def insert(s: str):
            cur = tri
            for c in s:
                if c not in cur:
                    cur[c] = Node(c)
                cur[c].count += 1
                cur = cur[c].next

        def score(s: str):
            cur = tri
            res = 0
            for c in s:
                if c in cur:
                    res += cur[c].count
                    cur = cur[c].next
                else:
                    break
            return res

        for word in words:
            insert(word)

        answer = []
        for word in words:
            answer.append(score(word))

        return answer
