import pytest
from solutions.sol_2864 import Solution

cases = [
    {
        "input": {
            "s": "010",
        },
        "output": "001",
    },
    {
        "input": {
            "s": "0101",
        },
        "output": "1001",
    },
]


@pytest.mark.sol_2864
def test_run():
    for case in cases:
        assert (
            Solution.maximum_odd_binary_number(s=case["input"]["s"]) == case["output"]
        )
