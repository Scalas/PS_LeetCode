from leet_code_types.leet_code_types import NestedInteger


class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.st = []
        self.current = nested_list
        self.idx = 0
        self.to_next()

    def next(self) -> int:
        res = self.current[self.idx].getInteger()
        self.idx += 1
        self.to_next()
        return res

    def to_next(self):
        if self.idx == len(self.current):
            if not self.st:
                return
            self.current, self.idx = self.st.pop()
        while self.current and not self.current[self.idx].isInteger():
            if self.idx < len(self.current) - 1:
                self.st.append((self.current, self.idx + 1))
            self.current, self.idx = self.current[self.idx].getList(), 0
        if self.idx >= len(self.current):
            return self.to_next()

    def has_next(self) -> bool:
        return self.idx < len(self.current)
