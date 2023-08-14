class Solution:
    @staticmethod
    def remove_stars(s: str) -> str:
        sq = []
        for c in s:
            if c == "*":
                if sq:
                    sq.pop()
            else:
                sq.append(c)
        return "".join(sq)
