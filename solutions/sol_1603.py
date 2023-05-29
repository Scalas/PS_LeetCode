class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slot = [big, medium, small]

    def add_car(self, car_type: int) -> bool:
        if self.slot[car_type - 1]:
            self.slot[car_type - 1] -= 1
            return True
        return False