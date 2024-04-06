class Solution:
    @staticmethod
    def make_good(s: str) -> str:
        res = []
        diff = ord("a") - ord("A")
        for c in s:
            if res:
                pre = ord(res[-1])
                cur = ord(c)
                if abs(pre - cur) == diff:
                    res.pop()
                    continue
            res.append(c)
        return "".join(res)
