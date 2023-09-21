import pytest
from solutions.sol_4 import Solution

cases = [
    {
        "input": {
            "nums1": [1, 3],
            "nums2": [2],
        },
        "output": 2.00000,
    },
    {
        "input": {
            "nums1": [1, 2],
            "nums2": [3, 4],
        },
        "output": 2.50000,
    },
]


@pytest.mark.sol4
def test_run():
    for case in cases:
        assert (
            Solution.find_median_sorted_arrays(
                nums1=case["input"]["nums1"], nums2=case["input"]["nums2"]
            )
            == case["output"]
        )
