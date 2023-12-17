from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.storage = defaultdict(list)
        self.food_info = dict()
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            heappush(self.storage[cuisine], [-rating, food])
            self.food_info[food] = (cuisine, rating)

    def change_rating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_info[food]
        if rating != newRating:
            self.food_info[food] = (cuisine, newRating)
            heappush(self.storage[cuisine], [-newRating, food])

    def highest_rated(self, cuisine: str) -> str:
        q = self.storage[cuisine]
        while q:
            rating, food = q[0]
            rating *= -1
            if rating != self.food_info[food][1]:
                heappop(q)
            else:
                break
        return q[0][1]
