import pytest
from solutions.sol_91 import Solution

cases = [
    {"input": {"s": "12"}, "output": 2},
    {"input": {"s": "226"}, "output": 3},
    {"input": {"s": "06"}, "output": 0},
    {"input": {"s": "100"}, "output": 0},
]


@pytest.mark.so91
def test_run():
    for case in cases:
        assert Solution.num_decoding(s=case["input"]["s"]) == case["output"]
