import pytest
from solutions.sol_2366 import Solution

cases = [
    {
        "input": {
            "nums": [3, 9, 3],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [1, 2, 3, 4, 5],
        },
        "output": 0,
    },
    {
        "input": {
            "nums": [9, 2, 7, 4, 11],
        },
        "output": 5,
    },
    {
        "input": {
            "nums": [17, 99, 2, 77, 23, 83, 521, 30],
        },
        "output": 87,
    },
]


@pytest.mark.sol_2360
def test_run():
    for case in cases:
        assert (
            Solution.minimum_replacement(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
