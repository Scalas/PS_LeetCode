class MyCalendarTwo:
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        ins, outs = {start: 1}, {end: 1}
        entries = {start, end}

        for u, v in self.cal:
            if not (start >= v or end <= u):
                ins[u] = ins.get(u, 0) + 1
                outs[v] = outs.get(v, 0) + 1
                entries.add(u)
                entries.add(v)
        count = 0
        for entry in sorted(entries):
            count = count + ins.get(entry, 0) - outs.get(entry, 0)
            if count > 2:
                return False
        self.cal.append([start, end])
        return True
