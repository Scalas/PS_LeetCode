import pytest
from solutions.sol_1863 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3],
        },
        "output": 6,
    },
    {
        "input": {
            "nums": [5, 1, 6],
        },
        "output": 28,
    },
    {
        "input": {
            "nums": [3, 4, 5, 6, 7, 8],
        },
        "output": 480,
    },
]


@pytest.mark.sol1863
def test_run():
    for case in cases:
        assert (
            Solution.subset_xor_sum(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
