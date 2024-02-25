import pytest
from solutions.sol_2709 import Solution

cases = [
    {
        "input": {
            "nums": [2, 3, 6],
        },
        "output": True,
    },
    {
        "input": {
            "nums": [3, 9, 5],
        },
        "output": False,
    },
    {
        "input": {
            "nums": [4, 3, 12, 8],
        },
        "output": True,
    },
    {
        "input": {
            "nums": [30, 30],
        },
        "output": True,
    },
    {
        "input": {
            "nums": [1, 1],
        },
        "output": False,
    },
    {
        "input": {
            "nums": [
                70,
                30,
                42,
                80,
                35,
                54,
                30,
                75,
                70,
                90,
                42,
                60,
                90,
                10,
                30,
                84,
                80,
                75,
                24,
                56,
                50,
                14,
                77,
                65,
                84,
                30,
                78,
                90,
                70,
                70,
                14,
                90,
                70,
                90,
                84,
                77,
                66,
                30,
                30,
                66,
                84,
                70,
            ],
        },
        "output": True,
    },
]


@pytest.mark.sol_2709
def test_run():
    for case in cases:
        assert (
            Solution.can_traverse_all_pairs(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
