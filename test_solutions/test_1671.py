import pytest
from solutions.sol_1671 import Solution


cases = [
    {
        "input": {"nums": [1, 3, 1]},
        "output": 0,
    },
    {
        "input": {"nums": [2, 1, 1, 5, 6, 2, 3, 1]},
        "output": 3,
    },
]


@pytest.mark.sol1671
def test_run():
    for case in cases:
        assert (
            Solution.minimum_mountain_removals(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
