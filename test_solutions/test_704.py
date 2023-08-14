import pytest
from solutions.sol_704 import Solution

cases = [
    {
        "input": {
            "nums": [-1, 0, 3, 5, 9, 12],
            "target": 9,
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [-1, 0, 3, 5, 9, 12],
            "target": 2,
        },
        "output": -1,
    },
]


@pytest.mark.sol_704
def test_run():
    for case in cases:
        assert (
            Solution.search(
                nums=case["input"]["nums"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
