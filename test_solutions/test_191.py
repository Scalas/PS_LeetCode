import pytest
from solutions.sol_191 import Solution

cases = [
    {"input": {"n": int("00000000000000000000000000001011", 2)}, "output": 3},
    {"input": {"n": int("00000000000000000000000010000000", 2)}, "output": 1},
    {"input": {"n": int("11111111111111111111111111111101", 2)}, "output": 31},
]


@pytest.mark.sol191
def test_run():
    for case in cases:
        assert Solution.hamming_weight(n=case["input"]["n"]) == case["output"]
