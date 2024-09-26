class MyCalendar:
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        check = True
        for u, v in self.cal:
            if not (start >= v or end <= u):
                check = False
                break
        if not check:
            return False
        self.cal.append([start, end])
        return True
