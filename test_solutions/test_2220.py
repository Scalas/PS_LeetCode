import pytest
from solutions.sol_2220 import Solution


cases = [
    {
        "input": {"start": 10, "goal": 7},
        "output": 3,
    },
    {
        "input": {"start": 3, "goal": 4},
        "output": 3,
    },
]


@pytest.mark.sol2220
def test_run():
    for case in cases:
        assert (
            Solution.min_bit_flips(
                start=case["input"]["start"],
                goal=case["input"]["goal"],
            )
            == case["output"]
        )
