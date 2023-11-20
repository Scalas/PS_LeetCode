from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def garbage_collection(garbage: List[str], travel: List[int]) -> int:
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        travel.append(0)
        m, p, g = 0, 0, 0
        mc, pc, gc = 0, 0, 0
        for i in range(len(garbage)):
            count = defaultdict(int)
            for c in garbage[i]:
                count[c] += 1
            if count["M"]:
                m = i
                mc += count["M"]
            if count["P"]:
                p = i
                pc += count["P"]
            if count["G"]:
                g = i
                gc += count["G"]
        return travel[m - 1] + travel[p - 1] + travel[g - 1] + mc + pc + gc
