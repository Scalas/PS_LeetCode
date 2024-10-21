class Solution:
    @staticmethod
    def parse_bool_expr(expression: str) -> bool:
        ops = []
        args = []
        for c in expression:
            if c == ",":
                continue
            if c == "(":
                args.append(c)
                continue
            if c == "t":
                args.append(True)
                continue
            if c == "f":
                args.append(False)
                continue
            if c == ")":
                op = ops.pop()
                if op == "!":
                    val = args.pop()
                    args.pop()
                    args.append(not val)
                elif op == "&":
                    res = True
                    while args[-1] != "(":
                        res = args.pop() and res
                    args.pop()
                    args.append(res)
                else:
                    res = False
                    while args[-1] != "(":
                        res = args.pop() or res
                    args.pop()
                    args.append(res)
                continue
            ops.append(c)
        return args[0]
