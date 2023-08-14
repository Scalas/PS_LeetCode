from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def count_sub_arrays(nums: List[int], min_k: int, max_k: int) -> int:
        def count_case(sub_nums: List[int]):
            min_index = []
            max_index = []
            for i in range(len(sub_nums)):
                if sub_nums[i] == min_k:
                    min_index.append(i)
                if sub_nums[i] == max_k:
                    max_index.append(i)
            if not min_index or not max_index:
                return 0
            max_start = min(min_index[-1], max_index[-1])
            res = 0
            for start in range(max_start + 1):
                min_end = max(
                    min_index[bisect_left(min_index, start)],
                    max_index[bisect_left(max_index, start)],
                )
                res += len(sub_nums) - min_end
            return res

        answer = 0
        sub = []
        for i in range(len(nums)):
            if min_k <= nums[i] <= max_k:
                sub.append(nums[i])
            else:
                if sub:
                    answer += count_case(sub)
                sub = []
        if sub:
            answer += count_case(sub)
        return answer
