import pytest
from solutions.sol_309 import Solution

cases = [
    {"input": {"prices": [1, 2, 3, 0, 2]}, "output": 3},
    {"input": {"prices": [1]}, "output": 0},
    {"input": {"prices": [1, 2, 4]}, "output": 3},
]


@pytest.mark.sol_309
def test_run():
    for case in cases:
        assert Solution.max_profit(prices=case["input"]["prices"]) == case["output"]
