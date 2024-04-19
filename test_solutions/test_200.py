import pytest
from solutions.sol_200 import Solution

cases = [
    {
        "input": {
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        },
        "output": 1,
    },
    {
        "input": {
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
        },
        "output": 3,
    },
]


@pytest.mark.sol200
def test_run():
    for case in cases:
        assert (
            Solution.num_islands(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
