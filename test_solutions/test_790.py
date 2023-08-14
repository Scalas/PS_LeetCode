import pytest
from solutions.sol_790 import Solution

cases = [
    {"input": {"n": 3}, "output": 5},
    {"input": {"n": 1}, "output": 1},
]


@pytest.mark.sol_790
def test_run():
    for case in cases:
        assert Solution.num_tilings(n=case["input"]["n"]) == case["output"]
