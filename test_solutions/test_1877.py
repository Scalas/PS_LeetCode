import pytest
from solutions.sol_1877 import Solution

cases = [
    {
        "input": {
            "nums": [3, 5, 2, 3],
        },
        "output": 7,
    },
    {
        "input": {
            "nums": [3, 5, 4, 2, 4, 6],
        },
        "output": 8,
    },
]


@pytest.mark.sol1877
def test_run():
    for case in cases:
        assert (
            Solution.min_pair_sum(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
