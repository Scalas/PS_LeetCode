class ProductOfNumbers:
    def __init__(self):
        self.count = [[] for _ in range(101)]
        self.size = 0

    def add(self, num: int) -> None:
        for i in range(101):
            cnt = self.count[i]
            c = 1 if num == i else 0
            pre = cnt[-1] if cnt else 0
            cnt.append(c + pre)
        self.size += 1

    def get_product(self, k: int) -> int:
        r = self.size - 1
        l = r - k
        res = 1
        for i in range(101):
            cnt = self.count[i]
            c = cnt[r]
            if l >= 0:
                c -= cnt[l]
            if c > 0:
                res *= i**c
        return res
