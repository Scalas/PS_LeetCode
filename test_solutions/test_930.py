import pytest
from solutions.sol_930 import Solution

cases = [
    {
        "input": {
            "nums": [1, 0, 1, 0, 1],
            "goal": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [0, 0, 0, 0, 0],
            "goal": 0,
        },
        "output": 15,
    },
    {
        "input": {
            "nums": [0, 0, 0, 1, 0, 0],
            "goal": 1,
        },
        "output": 12,
    },
    {
        "input": {
            "nums": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            "goal": 0,
        },
        "output": 27,
    },
    {
        "input": {
            "nums": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "goal": 1,
        },
        "output": 0,
    },
]


@pytest.mark.sol930
def test_run():
    for case in cases:
        assert (
            Solution.num_sub_arrays_with_sum(
                nums=case["input"]["nums"],
                goal=case["input"]["goal"],
            )
            == case["output"]
        )
