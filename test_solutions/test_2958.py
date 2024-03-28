import pytest
from solutions.sol_2958 import Solution

cases = [
    {
        "input": {"nums": [1, 2, 3, 1, 2, 3, 1, 2], "k": 2},
        "output": 6,
    },
    {
        "input": {
            "nums": [1, 2, 1, 2, 1, 2, 1, 2],
            "k": 1,
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [5, 5, 5, 5, 5, 5, 5],
            "k": 4,
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [1],
            "k": 1,
        },
        "output": 1,
    },
]


@pytest.mark.sol_2958
def test_run():
    for case in cases:
        assert (
            Solution.max_sub_array_length(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
