class Solution:
    @staticmethod
    def winner_of_game(colors: str) -> bool:
        ac, bc = 0, 0
        buf = []
        for c in colors:
            if not buf:
                buf.append(c)
            else:
                if buf[-1] != c:
                    if c == "A":
                        bc += max(len(buf) - 2, 0)
                    else:
                        ac += max(len(buf) - 2, 0)
                    buf = []
                buf.append(c)
        if buf[0] == "A":
            ac += max(len(buf) - 2, 0)
        else:
            bc += max(len(buf) - 2, 0)
        return ac > bc
