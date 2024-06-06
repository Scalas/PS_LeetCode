import pytest
from solutions.sol_846 import Solution

cases = [
    {"input": {"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "group_size": 3}, "output": True},
    {"input": {"hand": [1, 2, 3, 4, 5], "group_size": 4}, "output": False},
]


@pytest.mark.sol846
def test_run():
    for case in cases:
        assert (
            Solution.is_n_straight_hand(
                hand=case["input"]["hand"], group_size=case["input"]["group_size"]
            )
            == case["output"]
        )
