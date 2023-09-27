class Solution:
    @staticmethod
    def decode_at_index(s: str, k: int) -> str:
        k -= 1
        slist = []
        buf = []
        num = 0
        for c in s:
            if c.isalpha():
                if not buf and num:
                    slist.append(num)
                    num = 0
                buf.append(c)
            else:
                if not num:
                    slist.append("".join(buf))
                    buf = []
                    num = int(c)
                else:
                    num *= int(c)
        if buf:
            slist.append("".join(buf))
        if num:
            slist.append(num)

        if len(slist) % 2:
            slist.append(1)

        r = [[slist[i], slist[i + 1], 0] for i in range(0, len(slist), 2)]
        pre = 0
        for i in range(len(r)):
            word, count, total = r[i]
            r[i][2] = (len(word) + pre) * count
            if r[i][2] > k:
                break
            pre = r[i][2]
        while r[-1][2] == 0:
            r.pop()

        while r:
            word, count, total = r.pop()
            prelen = 0 if not r else r[-1][2]
            baselen = prelen + len(word)
            idx = k % baselen
            if idx >= prelen:
                return word[idx - prelen]
            k = idx
        return ""
