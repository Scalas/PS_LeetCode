import pytest
from solutions.sol_260 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 1, 3, 2, 5],
        },
        "output": [3, 5],
    },
    {
        "input": {
            "nums": [-1, 0],
        },
        "output": [-1, 0],
    },
    {
        "input": {
            "nums": [0, 1],
        },
        "output": [0, 1],
    },
]


@pytest.mark.sol260
def test_run():
    for case in cases:
        assert sorted(
            Solution.single_number(
                nums=case["input"]["nums"],
            )
        ) == sorted(case["output"])
