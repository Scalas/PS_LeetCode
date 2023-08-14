import pytest
from solutions.sol_2551 import Solution

cases = [
    {
        "input": {
            "weights": [1, 3, 5, 1],
            "k": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "weights": [1, 3],
            "k": 2,
        },
        "output": 0,
    },
]


@pytest.mark.sol_2551
def test_run():
    for case in cases:
        assert (
            Solution.put_marbles(weights=case["input"]["weights"], k=case["input"]["k"])
            == case["output"]
        )
