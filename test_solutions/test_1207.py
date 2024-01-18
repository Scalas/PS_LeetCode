import pytest
from solutions.sol_1207 import Solution

cases = [
    {
        "input": {
            "arr": [1, 2, 2, 1, 1, 3],
        },
        "output": True,
    },
    {
        "input": {
            "arr": [1, 2],
        },
        "output": False,
    },
    {
        "input": {
            "arr": [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
        },
        "output": True,
    },
]


@pytest.mark.sol1207
def test_run():
    for case in cases:
        assert (
            Solution.unique_occurrences(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
