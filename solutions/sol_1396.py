class UndergroundSystem:
    def __init__(self):
        self.book = dict()
        self.history = dict()

    def check_in(self, customer_id: int, station_name: str, t: int) -> None:
        self.book[customer_id] = (station_name, t)

    def check_out(self, customer_id: int, station_name: str, t: int) -> None:
        start_station, start_time = self.book[customer_id]
        del self.book[customer_id]
        key = (start_station, station_name)
        if key not in self.history:
            self.history[key] = [0, 0]
        self.history[key][0] += t - start_time
        self.history[key][1] += 1

    def get_average_time(self, start_station: str, end_station: str) -> float:
        total, count = self.history[(start_station, end_station)]
        return total / count
