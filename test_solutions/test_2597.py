import pytest
from solutions.sol_2597 import Solution

cases = [
    {
        "input": {
            "nums": [2, 4, 6],
            "k": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [1],
            "k": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "nums": [4, 2, 5, 9, 10, 3],
            "k": 1,
        },
        "output": 23,
    },
    {
        "input": {
            "nums": [10, 4, 5, 7, 2, 1],
            "k": 3,
        },
        "output": 23,
    },
]


@pytest.mark.sol_2597
def test_run():
    for case in cases:
        assert (
            Solution.beautiful_subsets(nums=case["input"]["nums"], k=case["input"]["k"])
            == case["output"]
        )
