import pytest
from solutions.sol_198 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 3, 1],
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [2, 7, 9, 3, 1],
        },
        "output": 12,
    },
]


@pytest.mark.sol198
def test_run():
    for case in cases:
        assert (
            Solution.rob(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
