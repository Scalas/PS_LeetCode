from typing import List


class Solution:
    @staticmethod
    def number_of_beams(bank: List[str]) -> int:
        return (lambda y: sum([y[i] * y[i + 1] for i in range(len(y) - 1)]))(
            [c for c in map(lambda x: x.count("1"), bank) if c != 0]
        )
