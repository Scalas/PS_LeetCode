class Solution:
    operator = {"+": 0, "-": 0, "*": 1, "/": 1}

    @staticmethod
    def calculate(s: str) -> int:
        tokens = Solution.tokenize(s)
        st = [tokens[0]]
        op = []

        for i in range(1, len(tokens), 2):
            e = tokens[i]
            while op and Solution.operator[op[-1]] >= Solution.operator[e]:
                o2, o1 = st.pop(), st.pop()
                oprt = op.pop()
                st.append(Solution.operation(o1, o2, oprt))
            st.append(tokens[i + 1])
            op.append(e)

        while op:
            o2, o1 = st.pop(), st.pop()
            oprt = op.pop()
            st.append(Solution.operation(o1, o2, oprt))

        return st[0]

    @staticmethod
    def tokenize(s: str):
        s = s.replace(" ", "")
        res = []
        buf = []
        for c in s:
            if c not in Solution.operator.keys():
                buf.append(c)
            else:
                res.append(int("".join(buf)))
                res.append(c)
                buf = []
        res.append(int("".join(buf)))
        return res

    @staticmethod
    def operation(oprd1, oprd2, operator):
        if operator == "+":
            return oprd1 + oprd2
        elif operator == "-":
            return oprd1 - oprd2
        elif operator == "*":
            return oprd1 * oprd2
        else:
            return oprd1 // oprd2
