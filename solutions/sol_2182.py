class Solution:
    @staticmethod
    def repeat_limited_string(s: str, repeat_limit: int) -> str:
        count = [0] * 26
        s = list(map(lambda x: ord(x) - ord("a"), s))
        for c in s:
            count[c] += 1

        res = []
        for i in range(25, -1, -1):
            for j in range(count[i]):
                if j % repeat_limit == 0 and j > 0:
                    nxt = -1
                    for k in range(i - 1, -1, -1):
                        if count[k] > 0:
                            nxt = k
                            break
                    if nxt == -1:
                        break
                    count[nxt] -= 1
                    res.append(nxt)
                count[i] -= 1
                res.append(i)
        return "".join(map(lambda x: chr(x + ord("a")), res))
