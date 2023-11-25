import pytest
from solutions.sol_1685 import Solution

cases = [
    {
        "input": {
            "nums": [2, 3, 5],
        },
        "output": [4, 3, 5],
    },
    {
        "input": {
            "nums": [1, 4, 6, 8, 10],
        },
        "output": [24, 15, 13, 15, 21],
    },
]


@pytest.mark.sol1685
def test_run():
    for case in cases:
        assert (
            Solution.get_sum_absolute_differences(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
