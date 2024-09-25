import pytest
from solutions.sol_3043 import Solution


cases = [
    {
        "input": {"arr1": [1, 10, 100], "arr2": [1000]},
        "output": 3,
    },
    {
        "input": {"arr1": [1, 2, 3], "arr2": [4, 4, 4]},
        "output": 0,
    },
]


@pytest.mark.sol3043
def test_run():
    for case in cases:
        assert (
            Solution.longest_common_prefix(
                arr2=case["input"]["arr2"],
                arr1=case["input"]["arr1"],
            )
            == case["output"]
        )
