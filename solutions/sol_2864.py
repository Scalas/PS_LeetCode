class Solution:
    @staticmethod
    def maximum_odd_binary_number(s: str) -> str:
        r = list(s)
        for i in range(len(r)):
            if r[i] == "1":
                r[i] = "0"
                break
        r.sort(reverse=True)
        r[-1] = "1"
        return "".join(r)
