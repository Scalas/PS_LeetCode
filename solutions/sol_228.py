from typing import List


class Solution:
    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        buf = []
        for num in nums:
            if not buf or buf[-1] == num - 1:
                if len(buf) < 2:
                    buf.append(num)
                else:
                    buf[1] = num
            else:
                if len(buf) == 1:
                    res.append(str(buf[0]))
                else:
                    res.append(f'{buf[0]}->{buf[1]}')
                buf = [num]
        if len(buf) == 1:
            res.append(str(buf[0]))
        else:
            res.append(f'{buf[0]}->{buf[1]}')
        return res
