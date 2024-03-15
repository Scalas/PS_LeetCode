import pytest
from solutions.sol_238 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 3, 4],
        },
        "output": [24, 12, 8, 6],
    },
    {
        "input": {
            "nums": [-1, 1, 0, -3, 3],
        },
        "output": [0, 0, 9, 0, 0],
    },
]


@pytest.mark.sol238
def test_run():
    for case in cases:
        assert (
            Solution.product_except_self(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
