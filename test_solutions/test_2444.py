import pytest
from solutions.sol_2444 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3, 5, 2, 7, 5],
            "min_k": 1,
            "max_k": 5,
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [1, 1, 1, 1],
            "min_k": 1,
            "max_k": 1,
        },
        "output": 10,
    },
    {
        "input": {
            "nums": [
                689862,
                297861,
                946099,
                25145,
                946099,
                647669,
                863241,
                886257,
                946099,
                25145,
                567132,
                484586,
                478308,
                427044,
                545054,
                25145,
                25145,
                25145,
                25145,
                25145,
            ],
            "min_k": 25145,
            "max_k": 946099,
        },
        "output": 122,
    },
]


@pytest.mark.sol_2444
def test_run():
    for case in cases:
        assert (
            Solution.count_sub_arrays(
                nums=case["input"]["nums"],
                min_k=case["input"]["min_k"],
                max_k=case["input"]["max_k"],
            )
            == case["output"]
        )
