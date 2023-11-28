import pytest
from solutions.sol_2147 import Solution

cases = [
    {
        "input": {"corridor": "SSPPSPS"},
        "output": 3,
    },
    {
        "input": {"corridor": "PPSPSP"},
        "output": 1,
    },
    {
        "input": {"corridor": "S"},
        "output": 0,
    },
    {
        "input": {"corridor": "P"},
        "output": 0,
    },
]


@pytest.mark.sol_2147
def test_run():
    for case in cases:
        assert (
            Solution.number_of_ways(
                corridor=case["input"]["corridor"],
            )
            == case["output"]
        )
