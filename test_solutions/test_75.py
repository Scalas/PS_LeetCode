import pytest
from solutions.sol_75 import Solution

cases = [
    {
        "input": {
            "nums": [2, 0, 2, 1, 1, 0],
        },
        "output": [0, 0, 1, 1, 2, 2],
    },
    {
        "input": {
            "nums": [2, 0, 1],
        },
        "output": [0, 1, 2],
    },
]


@pytest.mark.sol_75
def test_run():
    for case in cases:
        nums = case["input"]["nums"]
        Solution.sort_colors(
            nums=nums,
        )
        assert nums == case["output"]
