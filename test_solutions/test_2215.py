import pytest
from solutions.sol_2215 import Solution

cases = [
    {
        "input": {
            "nums1": [1, 2, 3],
            "nums2": [2, 4, 6],
        },
        "output": [[1, 3], [4, 6]],
    },
    {
        "input": {
            "nums1": [1, 2, 3, 3],
            "nums2": [1, 1, 2, 2],
        },
        "output": [[3], []],
    },
]


@pytest.mark.sol_2215
def test_run():
    for case in cases:
        assert (
            Solution.find_difference(
                nums1=case["input"]["nums1"],
                nums2=case["input"]["nums2"],
            )
            == case["output"]
        )
