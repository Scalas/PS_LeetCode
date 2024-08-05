from typing import List


class Solution:
    @staticmethod
    def count_seniors(details: List[str]) -> int:
        return len([1 for detail in details if int(detail[11:13]) > 60])
