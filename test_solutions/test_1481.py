import pytest
from solutions.sol_1481 import Solution

cases = [
    {
        "input": {
            "arr": [5, 5, 4],
            "k": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "arr": [4, 3, 1, 1, 3, 3, 2],
            "k": 3,
        },
        "output": 2,
    },
    {
        "input": {
            "arr": [1],
            "k": 1,
        },
        "output": 0,
    },
]


@pytest.mark.sol1481
def test_run():
    for case in cases:
        assert (
            Solution.find_least_num_of_unique_ints(
                arr=case["input"]["arr"], k=case["input"]["k"]
            )
            == case["output"]
        )
