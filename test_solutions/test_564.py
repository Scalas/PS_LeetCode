import pytest
from solutions.sol_564 import Solution


cases = [
    {
        "input": {"n": "123"},
        "output": "121",
    },
    {
        "input": {"n": "1"},
        "output": "0",
    },
]


@pytest.mark.sol564
def test_run():
    for case in cases:
        assert (
            Solution.nearest_palindromic(
                n=case["input"]["n"],
            )
            == case["output"]
        )
