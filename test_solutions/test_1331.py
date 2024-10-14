import pytest
from solutions.sol_1331 import Solution


cases = [
    {
        "input": {"arr": [40, 10, 20, 30]},
        "output": [4, 1, 2, 3],
    },
    {
        "input": {"arr": [100, 100, 100]},
        "output": [1, 1, 1],
    },
    {
        "input": {"arr": [37, 12, 28, 9, 100, 56, 80, 5, 12]},
        "output": [5, 3, 4, 2, 8, 6, 7, 1, 3],
    },
]


@pytest.mark.sol1331
def test_run():
    for case in cases:
        assert (
            Solution.array_rank_transform(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
