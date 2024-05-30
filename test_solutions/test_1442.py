import pytest
from solutions.sol_1442 import Solution

cases = [
    {
        "input": {
            "arr": [2, 3, 1, 6, 7],
        },
        "output": 4,
    },
    {
        "input": {
            "arr": [1, 1, 1, 1, 1],
        },
        "output": 10,
    },
]


@pytest.mark.sol1442
def test_run():
    for case in cases:
        assert Solution.count_triplets(arr=case["input"]["arr"]) == case["output"]
