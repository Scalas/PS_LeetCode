from collections import defaultdict


class Solution:
    @staticmethod
    def buddy_strings(s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = 0
        scnt, gcnt = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            scnt[s[i]] += 1
            gcnt[goal[i]] += 1
            if s[i] == goal[i]:
                continue
            if diff == 2:
                return False
            diff += 1
        for key in scnt:
            if scnt[key] != gcnt[key]:
                return False
        if not diff:
            return max(scnt.values()) >= 2
        if diff == 1:
            return False
        return True
