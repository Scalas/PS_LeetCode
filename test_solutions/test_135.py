import pytest
from solutions.sol_135 import Solution

cases = [
    {"input": {"ratings": [1, 0, 2]}, "output": 5},
    {"input": {"ratings": [1, 2, 2]}, "output": 4},
]


@pytest.mark.sol135
def test_run():
    for case in cases:
        assert Solution.candy(ratings=case["input"]["ratings"]) == case["output"]
