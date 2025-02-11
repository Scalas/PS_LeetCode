class Solution:
    @staticmethod
    def remove_occurrences(s: str, part: str) -> str:
        buf = []
        k = len(part)
        for c in s:
            buf.append(c)
            while len(buf) >= k:
                match = True
                for i in range(k):
                    if buf[-k + i] != part[i]:
                        match = False
                        break
                if match:
                    buf = buf[:-k]
                else:
                    break
        return "".join(buf)
