from collections import defaultdict
from heapq import heappush, heappop


class AllOne:
    def __init__(self):
        self.count = defaultdict(int)
        self.minq = []
        self.maxq = []

    def inc(self, key: str) -> None:
        self.count[key] += 1
        heappush(self.minq, [self.count[key], key])
        heappush(self.maxq, [-self.count[key], key])

    def dec(self, key: str) -> None:
        self.count[key] -= 1
        heappush(self.minq, [self.count[key], key])
        heappush(self.maxq, [-self.count[key], key])

    def get_max_key(self) -> str:
        while self.maxq:
            cnt, key = self.maxq[0]
            cnt *= -1
            if self.count[key] != cnt:
                heappop(self.maxq)
                continue
            else:
                return key
        return ""

    def get_min_key(self) -> str:
        while self.minq:
            cnt, key = self.minq[0]
            if cnt == 0 or self.count[key] != cnt:
                heappop(self.minq)
                continue
            else:
                return key
        return ""
