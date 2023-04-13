from typing import List


class Solution:
    @staticmethod
    def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)

        idx = 0
        st = []
        for num in pushed:
            st.append(num)
            while st and popped[idx] == st[-1]:
                st.pop()
                idx += 1

        return not st and idx == n
