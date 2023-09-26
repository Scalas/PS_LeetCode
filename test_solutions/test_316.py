import pytest
from solutions.sol_316 import Solution

cases = [
    {"input": {"s": "bcabc"}, "output": "abc"},
    {"input": {"s": "cbacdcbc"}, "output": "acdb"},
]


@pytest.mark.sol_316
def test_run():
    for case in cases:
        assert Solution.remove_duplicate_letters(s=case["input"]["s"]) == case["output"]
