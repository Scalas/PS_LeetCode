class Solution:
    @staticmethod
    def smallest_equivalent_string(s1: str, s2: str, base_str: str) -> str:
        s1 = list(map(Solution.to_ord, s1))
        s2 = list(map(Solution.to_ord, s2))
        base_str = list(map(Solution.to_ord, base_str))

        u = [-1] * 26
        for i in range(len(s1)):
            c1, c2 = s1[i], s2[i]
            Solution.union(u, c1, c2)

        return "".join(map(lambda x: Solution.to_str(Solution.find(u, x)), base_str))

    @staticmethod
    def to_ord(c: str):
        return ord(c) - ord("a")

    @staticmethod
    def to_str(c: int):
        return chr(c + ord("a"))

    @staticmethod
    def union(u, a, b):
        a = Solution.find(u, a)
        b = Solution.find(u, b)
        if a != b:
            if a < b:
                u[b] = a
            else:
                u[a] = b

    @staticmethod
    def find(u, x):
        if u[x] < 0:
            return x
        u[x] = Solution.find(u, u[x])
        return u[x]
