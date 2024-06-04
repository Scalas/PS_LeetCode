import pytest
from solutions.sol_3110 import Solution

cases = [
    {
        "input": {"s": "hello"},
        "output": 13,
    },
    {
        "input": {"s": "zaz"},
        "output": 50,
    },
]


@pytest.mark.sol_3110
def test_run():
    for case in cases:
        assert (
            Solution.score_of_string(
                s=case["input"]["s"],
            )
            == case["output"]
        )
