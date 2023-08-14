import pytest
from solutions.sol_605 import Solution

cases = [
    {"input": {"flowerbed": [1, 0, 0, 0, 1], "n": 1}, "output": True},
    {"input": {"flowerbed": [1, 0, 0, 0, 1], "n": 2}, "output": False},
]


@pytest.mark.sol_605
def test_run():
    for case in cases:
        assert (
            Solution.can_place_flowers(
                flowerbed=case["input"]["flowerbed"], n=case["input"]["n"]
            )
            == case["output"]
        )
