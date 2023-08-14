class SnapshotArray:
    def __init__(self, length: int):
        self.snapshot = [dict()]
        self.dirty = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[-1][index] = val
        self.dirty = 1

    def snap(self) -> int:
        if not self.dirty and len(self.snapshot) > 1:
            self.snapshot[-1] = self.snapshot[-2]
        self.snapshot.append(dict())
        self.dirty = 0
        return len(self.snapshot) - 2

    def get(self, index: int, snap_id: int) -> int:
        def find(sid, idx):
            if sid == -1:
                return 0
            val = self.snapshot[sid].get(idx, -1)
            if val != -1:
                return val
            self.snapshot[sid][idx] = find(sid - 1, idx)
            return self.snapshot[sid][idx]

        return find(snap_id, index)
