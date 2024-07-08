import pytest
from solutions.sol_1823 import Solution


cases = [
    {
        "input": {"n": 5, "k": 2},
        "output": 3,
    },
    {
        "input": {"n": 6, "k": 5},
        "output": 1,
    },
]


@pytest.mark.sol1823
def test_run():
    for case in cases:
        assert (
            Solution.find_the_winner(
                n=case["input"]["n"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
