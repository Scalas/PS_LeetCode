import pytest
from solutions.sol_2090 import Solution

cases = [
    {
        "input": {
            "nums": [7, 4, 3, 9, 1, 8, 5, 2, 6],
            "k": 3,
        },
        "output": [-1, -1, -1, 5, 4, 4, -1, -1, -1],
    },
    {
        "input": {
            "nums": [100000],
            "k": 0,
        },
        "output": [100000],
    },
    {
        "input": {
            "nums": [8],
            "k": 100000,
        },
        "output": [-1],
    },
]


@pytest.mark.sol_2090
def test_run():
    for case in cases:
        assert (
            Solution.get_averages(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
