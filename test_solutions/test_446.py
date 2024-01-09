import pytest
from solutions.sol_446 import Solution

cases = [
    {
        "input": {
            "nums": [2, 4, 6, 8, 10],
        },
        "output": 7,
    },
    {
        "input": {
            "nums": [7, 7, 7, 7, 7],
        },
        "output": 16,
    },
]


@pytest.mark.sol446
def test_run():
    for case in cases:
        assert (
            Solution.number_of_arithmetic_slices(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
