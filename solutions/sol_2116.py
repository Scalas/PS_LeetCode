class Solution:
    @staticmethod
    def can_be_valid(s: str, locked: str) -> bool:
        n = len(s)

        if n % 2:
            return False

        left, right = [], []
        free = []
        for i in range(n):
            if locked[i] == "1":
                if s[i] == "(":
                    left.append(i)
                else:
                    if left:
                        left.pop()
                    else:
                        right.append(i)
            else:
                free.append(i)

        if left:
            buf = free[::-1]
            for i in left:
                while buf and buf[-1] < i:
                    buf.pop()
                if not buf:
                    return False
                buf.pop()
        if right:
            buf = free[:]
            for i in right[::-1]:
                while buf and buf[-1] > i:
                    buf.pop()
                if not buf:
                    return False
                buf.pop()
        return True
