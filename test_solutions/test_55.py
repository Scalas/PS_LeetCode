import pytest
from solutions.sol_55 import Solution

cases = [
    {
        "input": {
            "nums": [2, 3, 1, 1, 4],
        },
        "output": True,
    },
    {
        "input": {
            "nums": [3, 2, 1, 0, 4],
        },
        "output": False,
    },
]


@pytest.mark.sol55
def test_run():
    for case in cases:
        assert (
            Solution.can_jump(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
