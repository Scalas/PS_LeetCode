from typing import List


class Solution:
    @staticmethod
    def can_place_flowers(flowerbed: List[int], n: int) -> bool:
        idx = 0
        fn = len(flowerbed)
        flowerbed.append(0)
        for _ in range(n):
            while idx < fn and flowerbed[idx - 1] + flowerbed[idx] + flowerbed[idx + 1]:
                idx += 1
            if idx == fn:
                return False
            flowerbed[idx] = 1
            idx += 1
        return True
