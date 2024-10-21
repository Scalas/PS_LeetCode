import pytest
from solutions.sol_2938 import Solution


cases = [
    {
        "input": {"s": "101"},
        "output": 1,
    },
    {
        "input": {"s": "100"},
        "output": 2,
    },
    {
        "input": {"s": "0111"},
        "output": 0,
    },
]


@pytest.mark.sol2938
def test_run():
    for case in cases:
        assert (
            Solution.minimum_steps(
                s=case["input"]["s"],
            )
            == case["output"]
        )
