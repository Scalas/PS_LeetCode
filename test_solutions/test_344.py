import pytest
from solutions.sol_344 import Solution

cases = [
    {"input": {"s": ["h", "e", "l", "l", "o"]}, "output": ["o", "l", "l", "e", "h"]},
    {
        "input": {"s": ["H", "a", "n", "n", "a", "h"]},
        "output": ["h", "a", "n", "n", "a", "H"],
    },
]


@pytest.mark.sol_344
def test_run():
    for case in cases:
        s = case["input"]["s"][:]
        Solution.reverse_string(s=s)
        assert s == case["output"]
