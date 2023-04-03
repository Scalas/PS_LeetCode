from typing import List


class Solution:
    @staticmethod
    def num_rescue_boats(people: List[int], limit: int) -> int:
        people.sort()

        s, e = 0, len(people) - 1
        answer = 0
        while s < e:
            sw = people[s]
            while e > s and people[e] > limit - sw:
                answer += 1
                e -= 1

            if s < e:
                answer += 1
                s += 1
                e -= 1
            else:
                break
        if s == e:
            answer += 1

        return answer
