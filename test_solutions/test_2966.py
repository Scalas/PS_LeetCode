import pytest
from solutions.sol_2966 import Solution

cases = [
    {
        "input": {"nums": [1, 3, 4, 8, 7, 9, 3, 5, 1], "k": 2},
        "output": [[1, 1, 3], [3, 4, 5], [7, 8, 9]],
    },
    {
        "input": {
            "nums": [1, 3, 3, 2, 7, 3],
            "k": 3,
        },
        "output": [],
    },
]


@pytest.mark.sol_2966
def test_run():
    for case in cases:
        assert (
            Solution.divide_array(nums=case["input"]["nums"], k=case["input"]["k"])
            == case["output"]
        )
