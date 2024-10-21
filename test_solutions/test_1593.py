import pytest
from solutions.sol_1593 import Solution


cases = [
    {
        "input": {"s": "ababccc"},
        "output": 5,
    },
    {
        "input": {"s": "aba"},
        "output": 2,
    },
    {
        "input": {"s": "aa"},
        "output": 1,
    },
]


@pytest.mark.sol1593
def test_run():
    for case in cases:
        assert (
            Solution.max_unique_split(
                s=case["input"]["s"],
            )
            == case["output"]
        )
