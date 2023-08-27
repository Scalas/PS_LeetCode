import pytest
from solutions.sol_403 import Solution

cases = [
    {
        "input": {
            "stones": [0, 1, 3, 5, 6, 8, 12, 17],
        },
        "output": True,
    },
    {
        "input": {
            "stones": [0, 1, 2, 3, 4, 8, 9, 11],
        },
        "output": False,
    },
]


@pytest.mark.sol403
def test_run():
    for case in cases:
        assert (
            Solution.can_cross(
                stones=case["input"]["stones"],
            )
            == case["output"]
        )
