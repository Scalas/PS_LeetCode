import pytest
from solutions.sol_338 import Solution

cases = [
    {"input": {"n": 2}, "output": [0, 1, 1]},
    {"input": {"n": 5}, "output": [0, 1, 1, 2, 1, 2]},
]


@pytest.mark.sol_338
def test_run():
    for case in cases:
        assert Solution.count_bits(n=case["input"]["n"]) == case["output"]
