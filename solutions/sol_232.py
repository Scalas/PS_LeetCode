class MyQueue:

    def __init__(self):
        self.st = []
        self.cursor = 0

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        res = self.st[self.cursor]
        self.cursor += 1
        return res

    def peek(self) -> int:
        return self.st[self.cursor]

    def empty(self) -> bool:
        return self.cursor >= len(self.st)
