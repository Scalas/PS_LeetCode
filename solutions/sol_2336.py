from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.retrieved = []
        self.have = set()

    def pop_smallest(self) -> int:
        if self.retrieved:
            res = heappop(self.retrieved)
            self.have.remove(res)
            return res
        else:
            res = self.cur
            self.cur += 1
            return res

    def add_back(self, num: int) -> None:
        if num < self.cur and num not in self.have:
            self.have.add(num)
            heappush(self.retrieved, num)
