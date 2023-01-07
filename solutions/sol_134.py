from typing import List


class Solution:
    @staticmethod
    def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        s, e = 0, 0
        remain_gas = 0
        while s < n and e - s < n:
            remain_gas += diff[e % n]
            e += 1
            while remain_gas < 0:
                remain_gas -= diff[s % n]
                s += 1
        return s if s < n else -1