class Solution:
    @staticmethod
    def maximum_gain(s: str, x: int, y: int) -> int:
        atoi = list(range(26))
        if x < y:
            atoi[0], atoi[1] = 1, 0
            x, y = y, x
        s = list(map(lambda x: atoi[ord(x) - ord("a")], s))
        st = []
        answer = 0
        for c in s:
            if c == 0:
                st.append(c)
            elif c == 1:
                if st and st[-1] == 0:
                    st.pop()
                    answer += x
                else:
                    st.append(c)
            else:
                tst = []
                for c in st:
                    if c == 1:
                        tst.append(c)
                    else:
                        if tst and tst[-1] == 1:
                            tst.pop()
                            answer += y
                        else:
                            tst.append(c)
                st = []
        tst = []
        for c in st:
            if c == 1:
                tst.append(c)
            else:
                if tst and tst[-1] == 1:
                    tst.pop()
                    answer += y
                else:
                    tst.append(c)
        return answer
