class Solution:
    @staticmethod
    def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
        q = [poured]
        row = 0
        if query_row == 0:
            return min(q[query_glass], 1)
        while True:
            row += 1
            nq = [max(q[0] - 1, 0) / 2]
            for i in range(len(q) - 1):
                nq.append((max(q[i] - 1, 0) + max(q[i + 1] - 1, 0)) / 2)
            nq.append(max(q[-1] - 1, 0) / 2)

            if row == query_row:
                return min(nq[query_glass], 1)

            if not sum(nq):
                break

            q = nq

        return 0
