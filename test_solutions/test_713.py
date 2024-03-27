import pytest
from solutions.sol_713 import Solution

cases = [
    {
        "input": {
            "nums": [10, 5, 2, 6],
            "k": 100,
        },
        "output": 8,
    },
    {
        "input": {
            "nums": [1, 2, 3],
            "k": 0,
        },
        "output": 0,
    },
    {
        "input": {
            "nums": [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3],
            "k": 19,
        },
        "output": 18,
    },
    {
        "input": {
            "nums": [100, 2, 3, 4, 100, 5, 6, 7, 100],
            "k": 100,
        },
        "output": 11,
    },
    {
        "input": {
            "nums": [1, 2, 3, 4, 5],
            "k": 1,
        },
        "output": 0,
    },
]


@pytest.mark.sol_713
def test_run():
    for case in cases:
        assert (
            Solution.num_sub_array_product_less_than_k(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
