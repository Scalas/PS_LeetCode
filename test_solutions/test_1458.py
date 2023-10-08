import pytest
from solutions.sol_1458 import Solution

cases = [
    {
        "input": {
            "nums1": [2, 1, -2, 5],
            "nums2": [3, 0, -6],
        },
        "output": 18,
    },
    {
        "input": {
            "nums1": [3, -2],
            "nums2": [2, -6, 7],
        },
        "output": 21,
    },
    {
        "input": {
            "nums1": [-1, -1],
            "nums2": [1, 1],
        },
        "output": -1,
    },
]


@pytest.mark.sol1458
def test_run():
    for case in cases:
        assert (
            Solution.max_dot_product(
                nums1=case["input"]["nums1"],
                nums2=case["input"]["nums2"],
            )
            == case["output"]
        )
