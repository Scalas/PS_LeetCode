from typing import List


class Solution:
    @staticmethod
    def min_operations(boxes: str) -> List[int]:
        n = len(boxes)
        boxes = list(map(int, boxes))
        answer = [0] * n
        acc = 0
        move = 0
        for i in range(n):
            move += acc
            answer[i] += move
            acc += boxes[i]

        acc = 0
        move = 0
        for i in range(n - 1, -1, -1):
            move += acc
            answer[i] += move
            acc += boxes[i]
        return answer
