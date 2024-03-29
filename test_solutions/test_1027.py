import pytest
from solutions.sol_1027 import Solution

cases = [
    {
        "input": {
            "nums": [3, 6, 9, 12],
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [9, 4, 7, 2, 10],
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [20, 1, 15, 3, 10, 5, 8],
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [
                1,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                1,
                0,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                0,
                1,
                0,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                1,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                1,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                1,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                0,
                1,
                0,
                1,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                1,
                1,
                0,
                1,
                0,
                1,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                1,
                1,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                0,
                1,
                0,
                0,
                0,
                1,
                1,
                1,
                1,
                1,
            ],
        },
        "output": 306,
    },
]


@pytest.mark.sol1027
def test_run():
    for case in cases:
        assert (
            Solution.longest_arith_seq_length(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
