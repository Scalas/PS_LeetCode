from typing import List


class Solution:
    @staticmethod
    def longest_square_streak(nums: List[int]) -> int:
        index = dict()
        nums.sort()
        n = len(nums)
        for i in range(n):
            index[nums[i]] = i

        answer = -1
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            streak = 1
            num = nums[i]
            low = num
            while True:
                sqrt = int(low**0.5)
                if sqrt**2 != low:
                    break
                if sqrt not in index:
                    break
                streak += 1
                visited[index[sqrt]] = True
                low = sqrt
            high = num
            while True:
                sq = high**2
                if sq not in index:
                    break
                streak += 1
                visited[index[sq]] = True
                high = sq
            if streak > 1:
                answer = max(answer, streak)

        return answer
