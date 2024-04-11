class Solution:
    @staticmethod
    def remove_k_digits(num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        st = []
        for c in num:
            d = int(c)
            while st and st[-1] > d and k:
                st.pop()
                k -= 1
            st.append(d)
        if k:
            st = st[:-k]
        z = 0
        while z < len(st) - 1 and st[z] == 0:
            z += 1
        st = st[z:]
        return "".join(map(str, st))
