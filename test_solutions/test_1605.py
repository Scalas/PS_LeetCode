import pytest
from solutions.sol_1605 import Solution


cases = [
    {
        "input": {"row_sum": [3, 8], "col_sum": [4, 7]},
    },
    {
        "input": {"row_sum": [5, 7, 10], "col_sum": [8, 6, 8]},
    },
]


@pytest.mark.sol1605
def test_run():
    for case in cases:
        row_sum, col_sum = case["input"]["row_sum"], case["input"]["col_sum"]
        mat = Solution.restore_matrix(
            row_sum=row_sum,
            col_sum=col_sum,
        )
        n, m = len(mat), len(mat[0])
        for i in range(n):
            assert sum(mat[i]) == row_sum[i]
        inv_mat = list(zip(*mat))
        for j in range(m):
            assert sum(inv_mat[j]) == col_sum[j]
        assert min(map(min, mat)) >= 0
