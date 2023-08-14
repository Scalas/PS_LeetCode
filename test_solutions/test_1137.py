import pytest
from solutions.sol_1137 import Solution

cases = [
    {"input": {"n": 4}, "output": 4},
    {"input": {"n": 25}, "output": 1389537},
    {"input": {"n": 2}, "output": 1},
]


@pytest.mark.sol1137
def test_run():
    for case in cases:
        assert Solution.tribonacci(n=case["input"]["n"]) == case["output"]
