import pytest
from solutions.sol_823 import Solution

cases = [
    {
        "input": {
            "arr": [2, 4],
        },
        "output": 3,
    },
    {
        "input": {
            "arr": [2, 4, 5, 10],
        },
        "output": 7,
    },
    {
        "input": {
            "arr": [2, 4, 8, 16],
        },
        "output": 23,
    },
]


@pytest.mark.sol_823
def test_run():
    for case in cases:
        assert (
            Solution.num_factored_binary_trees(arr=case["input"]["arr"])
            == case["output"]
        )
