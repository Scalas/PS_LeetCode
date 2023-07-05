from typing import List


class Solution:
    @staticmethod
    def longest_subarray(nums: List[int]) -> int:
        cluster = []
        start, length = -1, 0
        for i in range(len(nums)):
            if not nums[i]:
                if start != -1:
                    cluster.append((length, start))
                    start, length = -1, 0
                continue
            if start == -1:
                start, length = i, 1
            else:
                length += 1
        if start != -1:
            cluster.append((length, start))
        if not cluster:
            return 0
        answer = min(max(cluster)[0], len(nums) - 1)
        for i in range(len(cluster) - 1):
            cl, cs = cluster[i]
            nl, ns = cluster[i + 1]
            if ns - cs - cl == 1:
                answer = max(answer, cl + nl)
        return answer
