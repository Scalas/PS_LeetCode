import pytest
from solutions.sol_231 import Solution

cases = [
    {
        "input": {
            "n": 1,
        },
        "output": True,
    },
    {"input": {"n": 16}, "output": True},
    {"input": {"n": 3}, "output": False},
    {"input": {"n": 0}, "output": False},
    {"input": {"n": -16}, "output": False},
]


@pytest.mark.sol231
def test_run():
    for case in cases:
        assert Solution.is_power_of_two(n=case["input"]["n"]) == case["output"]
