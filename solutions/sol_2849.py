class Solution:
    @staticmethod
    def is_reachable_at_time(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        d = max(abs(fx - sx), abs(fy - sy))
        if not d:
            return t == 0 or t > 1
        return d <= t
