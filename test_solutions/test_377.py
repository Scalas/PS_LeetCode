import pytest
from solutions.sol_377 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 3],
            "target": 4,
        },
        "output": 7,
    },
    {
        "input": {
            "nums": [9],
            "target": 3,
        },
        "output": 0,
    },
]


@pytest.mark.sol377
def test_run():
    for case in cases:
        assert (
            Solution.combination_sum4(
                nums=case["input"]["nums"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
