from heapq import heappush, heappop


class LFUCache:
    def __init__(self, capacity: int):
        self.count = dict()
        self.recently_used = dict()
        self.value = dict()
        self.q = []
        self.size = 0
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        self.time += 1
        res = self.value.get(key, -1)
        if res != -1:
            self.count[key] += 1
            self.recently_used[key] = self.time
            heappush(self.q, (self.count[key], self.time, key))
        return res

    def put(self, key: int, value: int) -> None:
        self.time += 1
        if key in self.value:
            self.value[key] = value
            self.count[key] += 1
            self.recently_used[key] = self.time
            heappush(self.q, (self.count[key], self.time, key))
            return
        while self.size >= self.capacity:
            if not self.q:
                return
            c, t, k = heappop(self.q)
            if self.recently_used[k] != t:
                continue
            del self.count[k]
            del self.recently_used[k]
            del self.value[k]
            self.size -= 1
        self.count[key] = 1
        self.recently_used[key] = self.time
        self.value[key] = value
        heappush(self.q, (1, self.time, key))
        self.size += 1
