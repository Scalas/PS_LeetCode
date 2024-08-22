import pytest
from solutions.sol_476 import Solution


cases = [
    {
        "input": {"num": 5},
        "output": 2,
    },
    {
        "input": {"num": 1},
        "output": 0,
    },
]


@pytest.mark.sol476
def test_run():
    for case in cases:
        assert (
            Solution.find_complement(
                num=case["input"]["num"],
            )
            == case["output"]
        )
