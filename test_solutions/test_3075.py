import pytest
from solutions.sol_3075 import Solution

cases = [
    {
        "input": {"happiness": [1, 2, 3], "k": 2},
        "output": 4,
    },
    {
        "input": {"happiness": [1, 1, 1, 1], "k": 2},
        "output": 1,
    },
    {
        "input": {"happiness": [2, 3, 4, 5], "k": 1},
        "output": 5,
    },
]


@pytest.mark.sol_3075
def test_run():
    for case in cases:
        assert (
            Solution.maximum_happiness_sum(
                happiness=case["input"]["happiness"], k=case["input"]["k"]
            )
            == case["output"]
        )
