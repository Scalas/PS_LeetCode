import pytest
from solutions.sol_2696 import Solution


cases = [
    {
        "input": {"s": "ABFCACDB"},
        "output": 2,
    },
    {
        "input": {"s": "ACBBD"},
        "output": 5,
    },
]


@pytest.mark.sol2696
def test_run():
    for case in cases:
        assert (
            Solution.min_length(
                s=case["input"]["s"],
            )
            == case["output"]
        )
