from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def find_length_of_shortest_subarray(arr: List[int]) -> int:
        n = len(arr)
        left, right = [], []
        for num in arr:
            if not left or num >= left[-1]:
                left.append(num)
            else:
                break
        if len(left) == n:
            return 0
        for num in arr[::-1]:
            if not right or num <= right[-1]:
                right.append(num)
            else:
                break
        right = right[::-1]
        answer = min(n - len(left), n - len(right))
        for i in range(len(left)):
            l = i + 1
            r = len(right) - bisect_left(right, left[i])
            answer = min(answer, n - (l + r))
        return answer
