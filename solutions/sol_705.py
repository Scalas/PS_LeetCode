class MyHashSet:

    def __init__(self):
        self.bucket = [0] * 1000001

    def add(self, key: int) -> None:
        self.bucket[key] = 1

    def remove(self, key: int) -> None:
        self.bucket[key] = 0

    def contains(self, key: int) -> bool:
        return self.bucket[key] == 1
