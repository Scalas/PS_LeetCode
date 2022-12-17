from typing import List


class Solution:
    @staticmethod
    def eval_rpn(tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in '+-*/':
                o2, o1 = st.pop(), st.pop()
                if token == '+':
                    st.append(o1 + o2)
                elif token == '-':
                    st.append(o1 - o2)
                elif token == '*':
                    st.append(o1 * o2)
                else:
                    sign = 1 if o1 * o2 > 0 else -1
                    value = abs(o1) // abs(o2)
                    st.append(value * sign)
            else:
                st.append(int(token))
        return st[0]
