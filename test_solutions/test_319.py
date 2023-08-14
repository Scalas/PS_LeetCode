import pytest
from solutions.sol_319 import Solution

cases = [
    {"input": {"n": 3}, "output": 1},
    {"input": {"n": 0}, "output": 0},
    {"input": {"n": 1}, "output": 1},
]


@pytest.mark.sol_319
def test_run():
    for case in cases:
        assert Solution.bulb_switch(n=case["input"]["n"]) == case["output"]
