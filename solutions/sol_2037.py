from typing import List


class Solution:
    @staticmethod
    def min_moves_to_seat(seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(seats[i] - students[i]) for i in range(len(seats))])
