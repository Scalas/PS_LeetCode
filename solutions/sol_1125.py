from typing import List


class Solution:
    @staticmethod
    def smallest_sufficient_team(req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_map = dict()
        INF = 10 ** 9
        bit = 1
        people_bit = []
        for skills in people:
            skill_set = 0
            for skill in skills:
                if skill not in skill_map:
                    skill_map[skill] = bit
                    bit <<= 1
                skill_set |= skill_map[skill]
            people_bit.append(skill_set)

        req_skill_set = 0
        for skill in req_skills:
            req_skill_set |= skill_map[skill]

        n = len(people)

        dp = [[[-1, -1] for _ in range(bit)] for _ in range(n)]

        def dfs(cur, skill_set):
            if cur == n:
                res = 0 if skill_set | req_skill_set == skill_set else INF
                return [res, -1]
            if dp[cur][skill_set][0] == -1:
                res, idx = INF, -1
                # include
                nxt_min, nxt_idx = dfs(cur + 1, skill_set | people_bit[cur])
                if nxt_min != INF:
                    if nxt_min + 1 < res:
                        res = nxt_min + 1
                        idx = cur

                # not_include
                nxt_min, nxt_idx = dfs(cur + 1, skill_set)
                if nxt_min != INF:
                    if nxt_min < res:
                        res = nxt_min
                        idx = nxt_idx
                dp[cur][skill_set] = [res, idx]
            return dp[cur][skill_set]

        min_team, nxt = dfs(0, 0)
        answer = []
        state = 0
        while nxt != -1:
            answer.append(nxt)
            state |= people_bit[nxt]
            nxt = dfs(nxt + 1, state)[1]
        return answer
