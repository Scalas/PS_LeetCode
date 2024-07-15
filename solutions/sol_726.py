from collections import defaultdict


class Solution:
    @staticmethod
    def count_of_atoms(formula: str) -> str:
        tokens = []
        buf = []
        for c in formula:
            if c.islower():
                buf.append(c)
            elif c.isupper():
                if buf:
                    tokens.append("".join(buf))
                    buf = [c]
                else:
                    buf.append(c)
            elif c.isdigit():
                if buf:
                    if buf[-1].isdigit():
                        buf.append(c)
                    else:
                        tokens.append("".join(buf))
                        buf = [c]
                else:
                    buf.append(c)
            else:
                if buf:
                    tokens.append("".join(buf))
                    buf = []
                tokens.append(c)
        if buf:
            tokens.append("".join(buf))

        st = []
        for token in tokens:
            if token.isalpha():
                st.append([token, 1])
            elif token.isdigit():
                num = int(token)
                if st[-1][0].isalpha():
                    st[-1].append(num)
                else:
                    st.pop()
                    for i in range(len(st) - 1, -1, -1):
                        if st[i][0] == "(":
                            st[i][0] = "|"
                            break
                        st[i].append(num)
            else:
                st.append([token, -1])
        count = defaultdict(int)
        for token, *counts in st:
            cnt = 1
            for c in counts:
                cnt *= c
            if token.isalpha():
                count[token] += cnt

        answer = []
        for atom, cnt in sorted(count.items()):
            answer.append(atom)
            if cnt > 1:
                answer.append(str(cnt))
        return "".join(answer)
