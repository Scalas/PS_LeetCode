class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        if res != -1:
            del self.cache[key]
            self.cache[key] = res
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
            return
        if len(self.cache.keys()) == self.capacity:
            for k in self.cache.keys():
                del self.cache[k]
                break
        self.cache[key] = value
