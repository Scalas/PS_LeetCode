import pytest
from solutions.sol_42 import Solution

cases = [
    {"input": {"height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]}, "output": 6},
    {"input": {"height": [4, 2, 0, 3, 2, 5]}, "output": 9},
]


@pytest.mark.sol42
def test_run():
    for case in cases:
        assert Solution.trap(height=case["input"]["height"]) == case["output"]
