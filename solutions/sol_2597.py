from typing import List


class Solution:
    @staticmethod
    def beautiful_subsets(nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0

        def dfs(cur, st):
            nonlocal answer
            if cur == n:
                for basis in st.keys():
                    if st.get(basis + k, 0) or st.get(basis - k, 0):
                        return
                answer += 1
                return
            num = nums[cur]
            st[num] = st.get(num, 0) + 1
            dfs(cur + 1, st)
            st[num] -= 1
            if st[num] == 0:
                del st[num]
            dfs(cur + 1, st)

        dfs(0, {})
        return answer - 1
