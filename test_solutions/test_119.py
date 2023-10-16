import pytest
from solutions.sol_119 import Solution

cases = [
    {
        "input": {
            "row_index": 3,
        },
        "output": [1, 3, 3, 1],
    },
    {
        "input": {
            "row_index": 0,
        },
        "output": [1],
    },
    {
        "input": {
            "row_index": 1,
        },
        "output": [1, 1],
    },
]


@pytest.mark.sol119
def test_run():
    for case in cases:
        assert Solution.get_row(row_index=case["input"]["row_index"]) == case["output"]
