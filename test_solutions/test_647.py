import pytest
from solutions.sol_647 import Solution

cases = [
    {"input": {"s": "abc"}, "output": 3},
    {"input": {"s": "aaa"}, "output": 6},
]


@pytest.mark.sol_647
def test_run():
    for case in cases:
        assert (
            Solution.count_substrings(
                s=case["input"]["s"],
            )
            == case["output"]
        )
