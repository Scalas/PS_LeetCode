import pytest

from solutions.sol_1122 import Solution

cases = [
    {
        "input": {
            "arr1": [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            "arr2": [2, 1, 4, 3, 9, 6],
        },
        "output": [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    },
    {
        "input": {"arr1": [28, 6, 22, 8, 44, 17], "arr2": [22, 28, 8, 6]},
        "output": [22, 28, 8, 6, 17, 44],
    },
]


@pytest.mark.sol1122
def test_run():
    for case in cases:
        assert (
            Solution.relative_sort_array(
                arr1=case["input"]["arr1"],
                arr2=case["input"]["arr2"],
            )
            == case["output"]
        )
