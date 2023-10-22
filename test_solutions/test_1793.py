import pytest
from solutions.sol_1793 import Solution

cases = [
    {
        "input": {
            "nums": [1, 4, 3, 7, 4, 5],
            "k": 3,
        },
        "output": 15,
    },
    {
        "input": {
            "nums": [5, 5, 4, 5, 4, 1, 1, 1],
            "k": 0,
        },
        "output": 20,
    },
]


@pytest.mark.sol1793
def test_run():
    for case in cases:
        assert (
            Solution.maximum_score(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
