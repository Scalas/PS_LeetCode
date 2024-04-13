import pytest
from solutions.sol_85 import Solution

cases = [
    {
        "input": {
            "matrix": [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
        },
        "output": 6,
    },
    {
        "input": {
            "matrix": [["0"]],
        },
        "output": 0,
    },
    {
        "input": {
            "matrix": [["1"]],
        },
        "output": 1,
    },
]


@pytest.mark.sol85
def test_run():
    for case in cases:
        assert (
            Solution.maximal_rectangle(
                matrix=case["input"]["matrix"],
            )
            == case["output"]
        )
