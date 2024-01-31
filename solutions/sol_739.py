from typing import List


class Solution:
    @staticmethod
    def daily_temperatures(temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        st = []
        for i in range(n):
            t = temperatures[i]
            while st and st[-1][0] < t:
                pt, pi = st.pop()
                answer[pi] = i - pi
            st.append([t, i])
        return answer
