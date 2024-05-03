class Solution:
    @staticmethod
    def compare_version(version1: str, version2: str) -> int:
        u, v = map(lambda x: list(map(int, x.split("."))), [version1, version2])
        while len(u) < len(v):
            u.append(0)
        while len(v) < len(u):
            v.append(0)
        if u < v:
            return -1
        if u > v:
            return 1
        return 0
