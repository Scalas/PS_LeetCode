import pytest
from solutions.sol_287 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3, 4, 2, 2],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [3, 1, 3, 4, 2],
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [2, 2, 2, 2, 2],
        },
        "output": 2,
    },
]


@pytest.mark.sol287
def test_run():
    for case in cases:
        assert (
            Solution.find_duplicate(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
