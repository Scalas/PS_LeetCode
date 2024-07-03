import pytest
from solutions.sol_350 import Solution


cases = [
    {
        "input": {"nums1": [1, 2, 2, 1], "nums2": [2, 2]},
        "output": [2, 2],
    },
    {
        "input": {"nums1": [4, 9, 5], "nums2": [9, 4, 9, 8, 4]},
        "output": [4, 9],
    },
]


@pytest.mark.sol350
def test_run():
    for case in cases:
        assert sorted(
            Solution.intersect(
                nums2=case["input"]["nums2"],
                nums1=case["input"]["nums1"],
            )
        ) == sorted(case["output"])
