from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        self.size += 1

    def pop(self) -> int:
        for _ in range(self.size - 1):
            self.q.appendleft(self.q.pop())
        res = self.q.pop()
        self.size -= 1
        return res

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.size == 0
