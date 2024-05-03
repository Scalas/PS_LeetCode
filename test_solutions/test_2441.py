import pytest
from solutions.sol_2441 import Solution

cases = [
    {
        "input": {
            "nums": [-1, 2, -3, 3],
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [-1, 10, 6, 7, -7, 1],
        },
        "output": 7,
    },
    {
        "input": {
            "nums": [-10, 8, 6, 7, -2, -3],
        },
        "output": -1,
    },
]


@pytest.mark.sol_2441
def test_run():
    for case in cases:
        assert (
            Solution.find_max_k(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
