class Solution:
    @staticmethod
    def min_swaps(s: str) -> int:
        st = []
        answer = 0
        for c in s:
            if c == "[":
                st.append(c)
            else:
                if st:
                    st.pop()
                else:
                    st.append("[")
                    answer += 1
        return answer
