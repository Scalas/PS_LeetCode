from typing import List


class SummaryRanges:
    def __init__(self):
        self.arr = dict()
        self.range = dict()

    def _union(self, a, b):
        a = self._find(a)
        b = self._find(b)
        if a != b:
            if a < b:
                self.arr[a] += self.arr[b]
                self.arr[b] = a
                self.range[a] = self.range[b]
                del self.range[b]
            else:
                self.arr[b] += self.arr[a]
                self.arr[a] = b
                self.range[b] = self.range[a]
                del self.range[a]

    def _find(self, x):
        if self.arr[x] < 0:
            return x
        self.arr[x] = self._find(self.arr[x])
        return self.arr[x]

    def add_num(self, value: int) -> None:
        if value in self.arr:
            return
        self.arr[value] = -1
        self.range[value] = value
        if self.arr.get(value - 1, None) is not None:
            self._union(value - 1, value)
        if self.arr.get(value + 1, None) is not None:
            self._union(value + 1, value)

    def get_intervals(self) -> List[List[int]]:
        return sorted(self.range.items())
