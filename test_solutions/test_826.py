import pytest
from solutions.sol_826 import Solution

cases = [
    {
        "input": {
            "difficulty": [2, 4, 6, 8, 10],
            "profit": [10, 20, 30, 40, 50],
            "worker": [4, 5, 6, 7],
        },
        "output": 100,
    },
    {
        "input": {
            "difficulty": [85, 47, 57],
            "profit": [24, 66, 99],
            "worker": [40, 25, 25],
        },
        "output": 0,
    },
]


@pytest.mark.sol_826
def test_run():
    for case in cases:
        assert (
            Solution.max_profit_assignment(
                difficulty=case["input"]["difficulty"],
                profit=case["input"]["profit"],
                worker=case["input"]["worker"],
            )
            == case["output"]
        )
