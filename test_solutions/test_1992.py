import pytest
from solutions.sol_1992 import Solution

cases = [
    {
        "input": {
            "land": [[1, 0, 0], [0, 1, 1], [0, 1, 1]],
        },
        "output": [[0, 0, 0, 0], [1, 1, 2, 2]],
    },
    {
        "input": {
            "land": [[1, 1], [1, 1]],
        },
        "output": [[0, 0, 1, 1]],
    },
    {
        "input": {
            "land": [[0]],
        },
        "output": [],
    },
]


@pytest.mark.sol_1992
def test_run():
    for case in cases:
        assert (
            Solution.find_farmland(
                land=case["input"]["land"],
            )
            == case["output"]
        )
