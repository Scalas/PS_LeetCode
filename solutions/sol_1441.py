from typing import List


class Solution:
    @staticmethod
    def build_array(target: List[int], n: int) -> List[str]:
        answer = []
        pre = 0
        for num in target:
            c = num - pre - 1
            answer += ["Push"] * c
            answer += ["Pop"] * c
            answer.append("Push")
            pre = num
        return answer
