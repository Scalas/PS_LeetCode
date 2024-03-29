import pytest
from solutions.sol_2962 import Solution

cases = [
    {
        "input": {"nums": [1, 3, 2, 3, 3], "k": 2},
        "output": 6,
    },
    {
        "input": {"nums": [1, 4, 2, 1], "k": 3},
        "output": 0,
    },
    {
        "input": {
            "nums": [
                61,
                23,
                38,
                23,
                56,
                40,
                82,
                56,
                82,
                82,
                82,
                70,
                8,
                69,
                8,
                7,
                19,
                14,
                58,
                42,
                82,
                10,
                82,
                78,
                15,
                82,
            ],
            "k": 2,
        },
        "output": 224,
    },
]


@pytest.mark.sol_2962
def test_run():
    for case in cases:
        assert (
            Solution.count_sub_arrays(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
