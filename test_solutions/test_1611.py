import pytest
from solutions.sol_1611 import Solution

cases = [
    {
        "input": {
            "n": 3,
        },
        "output": 2,
    },
    {
        "input": {
            "n": 6,
        },
        "output": 4,
    },
    {
        "input": {
            "n": 15,
        },
        "output": 10,
    },
]


@pytest.mark.sol1611
def test_run():
    for case in cases:
        assert Solution.minimum_one_bit_operations(
            n=case["input"]["n"]
        ) == case["output"]
