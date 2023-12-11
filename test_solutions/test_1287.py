import pytest
from solutions.sol_1287 import Solution

cases = [
    {
        "input": {
            "arr": [1, 2, 2, 6, 6, 6, 6, 7, 10],
        },
        "output": 6,
    },
    {
        "input": {
            "arr": [1, 1],
        },
        "output": 1,
    },
    {
        "input": {
            "arr": [1, 2, 3, 3],
        },
        "output": 3,
    },
]


@pytest.mark.sol1287
def test_run():
    for case in cases:
        assert (
            Solution.find_special_integer(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
