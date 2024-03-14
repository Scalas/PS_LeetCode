from typing import List


class Solution:
    @staticmethod
    def num_sub_arrays_with_sum(nums: List[int], goal: int) -> int:
        st = [0]
        oc = 0
        for num in nums:
            if num == 1:
                oc += 1
                st.append(0)
            else:
                st[-1] += 1
        if goal == 0:
            return sum(map(lambda x: x * (x + 1) // 2, st))
        if goal > oc:
            return 0
        answer = 0
        for i in range(oc - goal + 1):
            j = i + goal - 1
            answer += (st[i] + 1) * (st[j + 1] + 1)
        return answer
