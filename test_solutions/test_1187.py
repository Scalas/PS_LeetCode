import pytest
from solutions.sol_1187 import Solution

cases = [
    {
        "input": {
            "arr1": [1, 5, 3, 6, 7],
            "arr2": [1, 3, 2, 4],
        },
        "output": 1,
    },
    {
        "input": {
            "arr1": [1, 5, 3, 6, 7],
            "arr2": [4, 3, 1],
        },
        "output": 2,
    },
    {
        "input": {
            "arr1": [1, 5, 3, 6, 7],
            "arr2": [1, 6, 3, 3],
        },
        "output": -1,
    },
]


@pytest.mark.sol1187
def test_run():
    for case in cases:
        assert (
            Solution.make_array_increasing(
                arr1=case["input"]["arr1"],
                arr2=case["input"]["arr2"],
            )
            == case["output"]
        )
