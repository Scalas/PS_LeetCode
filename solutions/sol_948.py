from typing import List


class Solution:
    @staticmethod
    def bag_of_tokens_score(tokens: List[int], power: int) -> int:
        n = len(tokens)
        s, e = 0, n - 1
        answer = 0
        point = 0
        tokens.sort()
        while s <= e:
            while s <= e and power < tokens[s] and point > 0:
                point -= 1
                power += tokens[e]
                e -= 1
            if s > e:
                break
            if power < tokens[s]:
                break
            point += 1
            power -= tokens[s]
            s += 1
            answer = max(answer, point)
            if s > e:
                break
        return answer
