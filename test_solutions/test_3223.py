import pytest
from solutions.sol_3223 import Solution


cases = [
    {
        "input": {"s": "abaacbcbb"},
        "output": 5,
    },
    {
        "input": {"s": "aa"},
        "output": 2,
    },
]


@pytest.mark.sol3223
def test_run():
    for case in cases:
        assert (
            Solution.minimum_length(
                s=case["input"]["s"],
            )
            == case["output"]
        )
