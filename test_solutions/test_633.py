import pytest

from solutions.sol_633 import Solution

cases = [
    {"input": {"c": 5}, "output": True},
    {"input": {"c": 3}, "output": False},
]


@pytest.mark.sol_633
def test_run():
    for case in cases:
        assert (
            Solution.judge_square_sum(
                c=case["input"]["c"],
            )
            == case["output"]
        )
