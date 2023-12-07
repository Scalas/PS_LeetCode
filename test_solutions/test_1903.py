import pytest
from solutions.sol_1903 import Solution

cases = [
    {
        "input": {
            "num": "35427",
        },
        "output": "35427",
    },
    {
        "input": {
            "num": "52",
        },
        "output": "5",
    },
    {
        "input": {
            "num": "4206",
        },
        "output": "",
    },
]


@pytest.mark.sol1903
def test_run():
    for case in cases:
        assert (
            Solution.largest_odd_number(
                num=case["input"]["num"],
            )
            == case["output"]
        )
