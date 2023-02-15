from typing import List


class Solution:
    @staticmethod
    def add_to_array_form(num: List[int], k: int) -> List[int]:
        return list(map(int, str(int(''.join(map(str, num))) + k)))
