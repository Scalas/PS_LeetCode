import pytest
from solutions.sol_2610 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3, 4, 1, 2, 3, 1],
        },
        "output": [[1, 3, 4, 2], [1, 3], [1]],
    },
    {
        "input": {
            "nums": [1, 2, 3, 4],
        },
        "output": [[1, 2, 3, 4]],
    },
]


@pytest.mark.sol_2551
def test_run():
    for case in cases:
        assert Solution.find_matrix(nums=case["input"]["nums"]) == case["output"]
