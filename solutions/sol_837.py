class Solution:
    @staticmethod
    def new_21_game(n: int, k: int, max_pts: int) -> float:
        if k == 0:
            return 1

        prob = [0.0] * (n + 2)
        prob[0] = 1
        hop = 1 / max_pts
        for i in range(1, n + 1):
            min_bound = max(i - max_pts, 0)
            if min_bound < k:
                max_bound = min(i - 1, k - 1)
                prob[i] = (prob[max_bound] - prob[min_bound - 1]) * hop
            prob[i] += prob[i - 1]
        return round(prob[n] - prob[k - 1], 5)
