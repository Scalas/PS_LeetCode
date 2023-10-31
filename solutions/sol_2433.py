from typing import List


class Solution:
    @staticmethod
    def find_array(pref: List[int]) -> List[int]:
        def xor(u, v):
            if u == v == 0:
                return 0

            if u < v:
                u, v = v, u

            cur = []
            while u:
                cur.append(u % 2)
                u //= 2

            target = []
            while v:
                target.append(v % 2)
                v //= 2
            target += [0] * (len(cur) - len(target))

            res = [1 - cur[i] if target[i] else cur[i] for i in range(len(cur))]

            return sum([res[i] * (1 << i) for i in range(len(res))])

        answer = []
        state = 0
        for num in pref:
            answer.append(xor(state, num))
            state = num
        return answer
