import pytest
from solutions.sol_1438 import Solution


cases = [
    {
        "input": {"nums": [8, 2, 4, 7], "limit": 4},
        "output": 2,
    },
    {
        "input": {"nums": [10, 1, 2, 4, 7, 2], "limit": 5},
        "output": 4,
    },
    {
        "input": {"nums": [4, 2, 2, 2, 4, 4, 2, 2], "limit": 0},
        "output": 3,
    },
]


@pytest.mark.sol1438
def test_run():
    for case in cases:
        assert (
            Solution.longest_subarray(
                limit=case["input"]["limit"],
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
