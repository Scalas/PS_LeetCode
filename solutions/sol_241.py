import re
from typing import List


class Solution:
    @staticmethod
    def diffWaysToCompute(expression: str) -> List[int]:
        answer = []
        ops = {"+", "-", "*"}
        operands = list(map(int, re.split("\+|-|\*", expression)))
        operators = [c for c in expression if c in ops]

        def calc(operand1, operand2, operator):
            if operator == "+":
                return operand1 + operand2
            if operator == "-":
                return operand1 - operand2
            return operand1 * operand2

        def dfs(oprds, oprts, start):
            nonlocal answer
            if len(oprds) == 1:
                answer.append(oprds[0])
                return
            for i in range(start, len(oprds) - 1):
                num = calc(oprds[i], oprds[i + 1], oprts[i])
                dfs(
                    oprds[:i] + [num] + oprds[i + 2 :],
                    oprts[:i] + oprts[i + 1 :],
                    max(i - 1, 0),
                )

        dfs(operands, operators, 0)

        return answer
