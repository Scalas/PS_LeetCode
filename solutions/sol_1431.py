from typing import List


class Solution:
    @staticmethod
    def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        maxv = max(candies)
        for i in range(len(candies)):
            answer.append(candies[i] + extraCandies >= maxv)
        
        return answer
