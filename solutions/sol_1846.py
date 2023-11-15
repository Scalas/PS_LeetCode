from typing import List


class Solution:
    @staticmethod
    def maximum_element_after_decrementing_and_rearranging(arr: List[int]) -> int:
        arr.sort()

        answer = 0
        for num in arr:
            if num > answer:
                answer += 1
        return answer
