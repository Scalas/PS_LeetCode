from typing import List


class Solution:
    @staticmethod
    def does_valid_array_exist(derived: List[int]) -> bool:
        def xor(o1, o2):
            return (~o1 & o2) | (o1 & ~o2)

        res = derived[0]
        for num in derived[1:]:
            res = xor(res, num)
        return res == 0
