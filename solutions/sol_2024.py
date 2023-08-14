class Solution:
    @staticmethod
    def max_consecutive_answers(answer_key: str, k: int) -> int:
        n = len(answer_key)
        tacc, facc = [], []
        tc, fc = 0, 0
        for v in answer_key:
            if v == "T":
                tc += 1
            else:
                fc += 1
            tacc.append(tc)
            facc.append(fc)
        tacc.append(0)
        facc.append(0)

        def check(val):
            for i in range(val - 1, n):
                # fill with T
                if facc[i] - facc[i - val] <= k:
                    return True
                if tacc[i] - tacc[i - val] <= k:
                    return True
            return False

        s, e = 0, n + 1
        answer = 0
        while s <= e:
            mid = (s + e) // 2
            if check(mid):
                answer = max(answer, mid)
                s = mid + 1
            else:
                e = mid - 1
        return answer
