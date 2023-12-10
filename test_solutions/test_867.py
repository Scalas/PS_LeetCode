import pytest
from solutions.sol_867 import Solution

cases = [
    {
        "input": {
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        "output": [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
    },
    {
        "input": {
            "matrix": [[1, 2, 3], [4, 5, 6]],
        },
        "output": [[1, 4], [2, 5], [3, 6]],
    },
]


@pytest.mark.sol867
def test_run():
    for case in cases:
        assert Solution.transpose(matrix=case["input"]["matrix"]) == case["output"]
