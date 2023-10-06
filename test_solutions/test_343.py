import pytest
from solutions.sol_343 import Solution

cases = [
    {"input": {"n": 2}, "output": 1},
    {"input": {"n": 10}, "output": 36},
    {"input": {"n": 3}, "output": 2},
    {"input": {"n": 8}, "output": 18},
]


@pytest.mark.sol_343
def test_run():
    for case in cases:
        assert Solution.integer_break(n=case["input"]["n"]) == case["output"]
