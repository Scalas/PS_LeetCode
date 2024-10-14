class CustomStack:
    def __init__(self, maxSize: int):
        self.cap = maxSize
        self.st = []

    def push(self, x: int) -> None:
        if len(self.st) < self.cap:
            self.st.append(x)

    def pop(self) -> int:
        if self.st:
            return self.st.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.st))):
            self.st[i] += val
