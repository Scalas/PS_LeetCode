class Solution:
    @staticmethod
    def min_length(s: str) -> int:
        st = []
        remove = {"AB", "CD"}
        for c in s:
            if st and st[-1] + c in remove:
                st.pop()
            else:
                st.append(c)
        return len(st)
