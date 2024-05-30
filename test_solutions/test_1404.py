import pytest
from solutions.sol_1404 import Solution

cases = [
    {
        "input": {
            "s": "1101",
        },
        "output": 6,
    },
    {
        "input": {
            "s": "10",
        },
        "output": 1,
    },
    {
        "input": {
            "s": "1",
        },
        "output": 0,
    },
]


@pytest.mark.sol1404
def test_run():
    for case in cases:
        assert Solution.num_steps(s=case["input"]["s"]) == case["output"]
