class Solution:
    @staticmethod
    def min_remove_to_make_valid(s: str) -> str:
        removed = [False] * len(s)
        p = []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                p.append(i)
            elif c == ")":
                if not p:
                    removed[i] = True
                else:
                    p.pop()
        for i in p:
            removed[i] = True
        return "".join([s[i] for i in range(len(s)) if not removed[i]])
