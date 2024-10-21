import pytest
from solutions.sol_670 import Solution


cases = [
    {
        "input": {"num": 2736},
        "output": 7236,
    },
    {
        "input": {"num": 9973},
        "output": 9973,
    },
]


@pytest.mark.sol670
def test_run():
    for case in cases:
        assert (
            Solution.maximum_swap(
                num=case["input"]["num"],
            )
            == case["output"]
        )
