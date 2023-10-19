class Solution:
    @staticmethod
    def backspace_compare(s: str, t: str) -> bool:
        sq = []
        tq = []
        for c in s:
            if c != "#":
                sq.append(c)
            elif sq:
                sq.pop()
        print(sq)

        for c in t:
            if c != "#":
                tq.append(c)
            elif tq:
                tq.pop()

        return sq == tq
