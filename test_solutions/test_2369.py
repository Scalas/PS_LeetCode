import pytest
from solutions.sol_2369 import Solution

cases = [
    {
        "input": {
            "nums": [4, 4, 4, 5, 6],
        },
        "output": True,
    },
    {
        "input": {
            "nums": [1, 1, 1, 2],
        },
        "output": False,
    },
    {
        "input": {
            "nums": [10, 20, 30],
        },
        "output": False,
    },
    {
        "input": {
            "nums": [
                579611,
                579611,
                579611,
                731172,
                731172,
                496074,
                496074,
                496074,
                151416,
                151416,
                151416,
            ],
        },
        "output": True,
    },
]


@pytest.mark.sol_2369
def test_run():
    for case in cases:
        assert (
            Solution.valid_partition(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
