class Solution:
    @staticmethod
    def reverse_parentheses(s: str) -> str:
        buf = [[]]
        for c in s:
            if c == "(":
                buf.append([])
            elif c == ")":
                rev = buf.pop()[::-1]
                buf[-1].extend(rev)
            else:
                buf[-1].append(c)
        return "".join(buf[0])
