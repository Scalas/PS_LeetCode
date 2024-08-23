class Solution:
    @staticmethod
    def fraction_addition(expression: str) -> str:
        child = []
        parent = []
        sign = []

        for expr in expression.split("+"):
            first, *remain = expr.split("-")
            if first == "":
                child.append(0)
                parent.append(1)
            else:
                c, p = first.split("/")
                child.append(int(c))
                parent.append(int(p))
            sign.append(1)
            for exp in remain:
                c, p = exp.split("/")
                child.append(int(c))
                parent.append(int(p))
                sign.append(-1)

        def gcd(x, y):
            if x < y:
                x, y = y, x
            while y:
                x, y = y, x % y
            return x

        common_parent = parent[0]
        for i in range(1, len(parent)):
            g = gcd(common_parent, parent[i])
            common_parent = common_parent * parent[i] // g

        total_child = 0
        for i in range(len(child)):
            total_child += child[i] * (common_parent // parent[i]) * sign[i]

        g = gcd(abs(common_parent), abs(total_child))

        return f"{total_child // g}/{common_parent // g}"
