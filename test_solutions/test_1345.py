import pytest
from solutions.sol_1345 import Solution

cases = [
    {
        "input": {
            "arr": [100, -23, -23, 404, 100, 23, 23, 23, 3, 404],
        },
        "output": 3,
    },
    {
        "input": {
            "arr": [7],
        },
        "output": 0,
    },
    {
        "input": {
            "arr": [7, 6, 9, 6, 9, 6, 9, 7],
        },
        "output": 1,
    },
]


@pytest.mark.sol1345
def test_run():
    for case in cases:
        assert Solution.min_jumps(arr=case["input"]["arr"]) == case["output"]
