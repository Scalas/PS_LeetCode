import pytest
from solutions.sol_921 import Solution


cases = [
    {
        "input": {"s": "())"},
        "output": 1,
    },
    {
        "input": {"s": "((("},
        "output": 3,
    },
]


@pytest.mark.sol921
def test_run():
    for case in cases:
        assert (
            Solution.min_add_to_make_valid(
                s=case["input"]["s"],
            )
            == case["output"]
        )
