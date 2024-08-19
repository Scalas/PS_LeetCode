import pytest
from solutions.sol_264 import Solution


cases = [
    {
        "input": {"n": 10},
        "output": 12,
    },
    {
        "input": {"n": 1},
        "output": 1,
    },
]


@pytest.mark.sol264
def test_run():
    for case in cases:
        assert (
            Solution.nth_ugly_number(
                n=case["input"]["n"],
            )
            == case["output"]
        )
