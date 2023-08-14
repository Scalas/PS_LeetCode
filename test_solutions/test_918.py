import pytest
from solutions.sol_918 import Solution

cases = [
    {
        "input": {
            "nums": [1, -2, 3, -2],
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [5, -3, 5],
        },
        "output": 10,
    },
    {
        "input": {
            "nums": [-3, -2, -3],
        },
        "output": -2,
    },
]


@pytest.mark.sol918
def test_run():
    for case in cases:
        assert (
            Solution.max_sub_array_sum_circular(nums=case["input"]["nums"])
            == case["output"]
        )
