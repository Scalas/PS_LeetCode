import pytest
from solutions.sol_525 import Solution

cases = [
    {
        "input": {"nums": [0, 1]},
        "output": 2,
    },
    {"input": {"nums": [0, 1, 0]}, "output": 2},
]


@pytest.mark.sol_525
def test_run():
    for case in cases:
        assert Solution.find_max_length(nums=case["input"]["nums"]) == case["output"]
