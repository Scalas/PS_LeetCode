class Solution:
    @staticmethod
    def make_fancy_string(s: str) -> str:
        st = []
        for c in s:
            if len(st) > 1 and st[-1] == st[-2] == c:
                continue
            st.append(c)
        return "".join(st)
