from typing import List


class Solution:
    @staticmethod
    def sum_subarray_mins(arr: List[int]) -> int:
        n = len(arr)
        limit = [[-1, -1] for _ in range(n)]

        st = [(-1, 0)]
        for i in range(n):
            num = arr[i]
            while num <= st[-1][1]:
                limit[st.pop()[0]][1] = i - 1
            st.append((i, num))
        for idx, _ in st[1:]:
            limit[idx][1] = n - 1

        st = [(-1, 0)]
        for i in range(n - 1, -1, -1):
            num = arr[i]
            while num < st[-1][1]:
                limit[st.pop()[0]][0] = i + 1
            st.append((i, num))
        for idx, _ in st[1:]:
            limit[idx][0] = 0

        answer = 0
        mod = 10**9 + 7
        for i in range(n):
            l, r = i - limit[i][0] + 1, limit[i][1] - i + 1
            answer = (answer + l * r * arr[i]) % mod
        return answer
