import pytest
from solutions.sol_2540 import Solution

cases = [
    {
        "input": {
            "nums1": [1, 2, 3],
            "nums2": [2, 4],
        },
        "output": 2,
    },
    {
        "input": {
            "nums1": [1, 2, 3, 6],
            "nums2": [2, 3, 4, 5],
        },
        "output": 2,
    },
]


@pytest.mark.sol_2492
def test_run():
    for case in cases:
        assert (
            Solution.get_common(
                nums1=case["input"]["nums1"], nums2=case["input"]["nums2"]
            )
            == case["output"]
        )
