import pytest
from solutions.sol_1464 import Solution

cases = [
    {
        "input": {
            "nums": [3, 4, 5, 2],
        },
        "output": 12,
    },
    {
        "input": {
            "nums": [1, 5, 4, 5],
        },
        "output": 16,
    },
    {
        "input": {
            "nums": [3, 7],
        },
        "output": 12,
    },
]


@pytest.mark.sol1464
def test_run():
    for case in cases:
        assert (
            Solution.max_product(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
