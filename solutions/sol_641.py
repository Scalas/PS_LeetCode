from collections import deque


class MyCircularDeque:
    def __init__(self, k: int):
        self.q = deque()
        self.size = k

    def insert_front(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.appendleft(value)
        return True

    def insert_last(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.append(value)
        return True

    def delete_front(self) -> bool:
        if not self.q:
            return False
        self.q.popleft()
        return True

    def delete_last(self) -> bool:
        if not self.q:
            return False
        self.q.pop()
        return True

    def get_front(self) -> int:
        return -1 if not self.q else self.q[0]

    def get_rear(self) -> int:
        return -1 if not self.q else self.q[-1]

    def is_empty(self) -> bool:
        return len(self.q) == 0

    def is_full(self) -> bool:
        return len(self.q) == self.size
