import pytest

from solutions.sol_342 import Solution

cases = [
    {"input": {"n": 16}, "output": True},
    {"input": {"n": 5}, "output": False},
    {"input": {"n": 1}, "output": True},
    {"input": {"n": 0}, "output": False},
]


@pytest.mark.sol_341
def test_run():
    for case in cases:
        assert Solution.is_power_of_four(n=case["input"]["n"]) == case["output"]
