import pytest
from solutions.sol_1913 import Solution

cases = [
    {
        "input": {
            "nums": [5, 6, 2, 7, 4],
        },
        "output": 34,
    },
    {
        "input": {
            "nums": [4, 2, 5, 9, 7, 4, 8],
        },
        "output": 64,
    },
]


@pytest.mark.sol1913
def test_run():
    for case in cases:
        assert (
            Solution.max_product_difference(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
