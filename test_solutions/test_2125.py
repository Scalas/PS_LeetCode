import pytest
from solutions.sol_2125 import Solution

cases = [
    {
        "input": {
            "bank": ["011001", "000000", "010100", "001000"],
        },
        "output": 8,
    },
    {
        "input": {
            "bank": ["000", "111", "000"],
        },
        "output": 0,
    },
]


@pytest.mark.sol_2125
def test_run():
    for case in cases:
        assert (
            Solution.number_of_beams(
                bank=case["input"]["bank"],
            )
            == case["output"]
        )
