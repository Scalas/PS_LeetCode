import pytest
from solutions.sol_2542 import Solution

cases = [
    {
        "input": {
            "nums1": [1, 3, 3, 2],
            "nums2": [2, 1, 3, 4],
            "k": 3,
        },
        "output": 12,
    },
    {
        "input": {
            "nums1": [4, 2, 3, 1, 1],
            "nums2": [7, 5, 10, 9, 6],
            "k": 1,
        },
        "output": 30,
    },
]


@pytest.mark.sol_2542
def test_run():
    for case in cases:
        assert (
            Solution.max_score(
                nums1=case["input"]["nums1"],
                nums2=case["input"]["nums2"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
