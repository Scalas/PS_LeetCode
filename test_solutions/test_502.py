import pytest
from solutions.sol_502 import Solution

cases = [
    {
        "input": {
            "k": 2,
            "w": 0,
            "profits": [1, 2, 3],
            "capital": [0, 1, 1],
        },
        "output": 4,
    },
    {
        "input": {
            "k": 3,
            "w": 0,
            "profits": [1, 2, 3],
            "capital": [0, 1, 2],
        },
        "output": 6,
    },
]


@pytest.mark.sol_502
def test_run():
    for case in cases:
        assert (
            Solution.find_maximized_capital(
                k=case["input"]["k"],
                w=case["input"]["w"],
                profits=case["input"]["profits"],
                capital=case["input"]["capital"],
            )
            == case["output"]
        )
