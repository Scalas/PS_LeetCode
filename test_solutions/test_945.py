import pytest
from solutions.sol_945 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 2],
        },
        "output": 1,
    },
    {
        "input": {
            "nums": [3, 2, 1, 2, 1, 7],
        },
        "output": 6,
    },
    {
        "input": {
            "nums": [0],
        },
        "output": 0,
    },
]


@pytest.mark.sol945
def test_run():
    for case in cases:
        assert (
            Solution.min_increment_for_unique(nums=case["input"]["nums"])
            == case["output"]
        )
