from typing import List


class Solution:
    @staticmethod
    def generate(num_rows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(num_rows - 1):
            line = [1]
            pre = res[-1]
            for i in range(len(pre) - 1):
                line.append(pre[i] + pre[i + 1])
            line.append(1)
            res.append(line)
        return res
