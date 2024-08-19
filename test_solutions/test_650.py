import pytest
from solutions.sol_650 import Solution


cases = [
    {
        "input": {"n": 3},
        "output": 3,
    },
    {
        "input": {"n": 1},
        "output": 0,
    },
]


@pytest.mark.sol650
def test_run():
    for case in cases:
        assert (
            Solution.min_steps(
                n=case["input"]["n"],
            )
            == case["output"]
        )
