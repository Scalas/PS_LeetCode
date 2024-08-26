from typing import List


class Solution:
    @staticmethod
    def nearest_palindromic(n: str) -> str:
        def decal(x: List[int]):
            half = len(x) // 2
            return (
                x[:half] + [x[half]] + x[:half][::-1]
                if len(x) % 2
                else x[:half] + x[:half][::-1]
            )

        def lower(x: List[int]):
            idx = len(x) // 2 if len(x) % 2 else len(x) // 2 - 1
            while idx >= 0 and x[idx] == 0:
                x[idx] = 9
                idx -= 1
            if idx >= 0:
                x[idx] -= 1
            else:
                x = x[1:]
            res = int("".join(map(str, decal(x))))
            if len(x) > 1:
                res = max(res, int("9" * (len(x) - 1)))
            return res

        def higher(x: List[int]):
            idx = len(x) // 2 if len(x) % 2 else len(x) // 2 - 1
            while idx >= 0 and x[idx] == 9:
                x[idx] = 0
                idx -= 1
            if idx >= 0:
                x[idx] += 1
            else:
                x = [1] + x
            res = int("".join(map(str, decal(x))))
            return res

        num = list(map(int, list(n)))
        pal_num_list = decal(num)
        pal_num = int("".join(map(str, pal_num_list)))
        lower_num = lower(pal_num_list[:])
        higher_num = higher(pal_num_list[:])
        cand = [lower_num, higher_num, pal_num]
        if pal_num_list == num:
            cand.pop()

        num = int(n)
        return str(min(cand, key=lambda x: (abs(num - x), x)))
