from leet_code_types.leet_code_types import MountainArray


class Solution:
    @staticmethod
    def find_in_mountain_array(target: int, mountain_arr: MountainArray) -> int:
        n = mountain_arr.length()
        INF = 10**9 + 1
        s, e = 0, n - 1
        midx = -1
        while s <= e:
            m = (s + e) // 2
            left = -1 if m == 0 else mountain_arr.get(m - 1)
            right = INF if m == n - 1 else mountain_arr.get(m + 1)
            cur = mountain_arr.get(m)
            if cur > left and cur > right:
                midx = m
                break
            if cur > left:
                s = m + 1
            else:
                e = m - 1

        if midx > 0:
            s, e = 0, midx
            while s <= e:
                m = (s + e) // 2
                val = mountain_arr.get(m)
                if val < target:
                    s = m + 1
                elif val > target:
                    e = m - 1
                else:
                    return m

        if midx <= n - 1:
            s, e = midx, n - 1
            while s <= e:
                m = (s + e) // 2
                val = mountain_arr.get(m)
                if val < target:
                    e = m - 1
                elif val > target:
                    s = m + 1
                else:
                    return m
        return -1
