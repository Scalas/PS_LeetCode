from random import randint

MIN_NUM = - 2 ** 31
MAX_NUM = 2 ** 31 - 1


class RandomizedSet:

    def __init__(self):
        self.rs = set()
        self.ls = []

    def insert(self, val: int) -> bool:
        if val in self.rs:
            return False
        self.rs.add(val)
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.rs:
            self.rs.remove(val)
            return True
        return False

    def get_random(self) -> int:
        val = self.ls[randint(0, len(self.ls) - 1)]
        while val not in self.rs:
            val = self.ls[randint(0, len(self.ls) - 1)]
        return val
