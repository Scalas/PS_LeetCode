class Solution:
    @staticmethod
    def is_scramble(s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 1:
            return s1 == s2

        alpha_mapper = lambda x: ord(x) - ord("a")
        s1 = list(map(alpha_mapper, s1))
        s2 = list(map(alpha_mapper, s2))

        mem = dict()

        def split(os, oe, s, e):
            key = (os, oe, s, e)
            if key in mem:
                return mem[key]
            if os == oe:
                return True

            olc, orc = [0] * 26, [0] * 26
            lc, rc = [0] * 26, [0] * 26

            k = e - s + 1
            same = True
            for i in range(k):
                oc, c = s1[os + i], s2[s + i]
                orc[oc] += 1
                rc[c] += 1
                if oc != c:
                    same = False

            if same:
                mem[key] = True
                return True

            if rc != orc:
                mem[key] = False
                return False

            # 순서를 바꾸지 않는 경우
            for i in range(k - 1):
                oc = s1[os + i]
                c = s2[s + i]
                olc[oc] += 1
                orc[oc] -= 1
                lc[c] += 1
                rc[c] -= 1
                if lc == olc:
                    if split(os, os + i, s, s + i) and split(
                        os + i + 1, oe, s + i + 1, e
                    ):
                        mem[key] = True
                        return True

            # 초기화
            for i in range(26):
                if orc[i]:
                    olc[i] += 1
                    orc[i] -= 1
                if rc[i]:
                    lc[i] += 1
                    rc[i] -= 1
            lc, rc, olc, orc = rc, lc, orc, olc

            # 순서를 바꾸는 경우
            for i in range(k - 1):
                oc = s1[oe - i]
                c = s2[s + i]
                olc[oc] += 1
                orc[oc] -= 1
                lc[c] += 1
                rc[c] -= 1
                if lc == olc:
                    if split(oe - i, oe, s, s + i) and split(
                        os, oe - i - 1, s + i + 1, e
                    ):
                        mem[key] = True
                        return True
            mem[key] = False
            return False

        return split(0, n - 1, 0, n - 1)
