import pytest
from solutions.sol_1963 import Solution


cases = [
    {
        "input": {"s": "][]["},
        "output": 1,
    },
    {
        "input": {"s": "]]][[["},
        "output": 2,
    },
    {
        "input": {"s": "[]"},
        "output": 0,
    },
]


@pytest.mark.sol1963
def test_run():
    for case in cases:
        assert (
            Solution.min_swaps(
                s=case["input"]["s"],
            )
            == case["output"]
        )
