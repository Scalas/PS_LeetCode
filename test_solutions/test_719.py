import pytest
from solutions.sol_719 import Solution


cases = [
    {
        "input": {"nums": [1, 3, 1], "k": 1},
        "output": 0,
    },
    {
        "input": {"nums": [1, 1, 1], "k": 2},
        "output": 0,
    },
    {
        "input": {"nums": [1, 6, 1], "k": 3},
        "output": 5,
    },
]


@pytest.mark.sol719
def test_run():
    for case in cases:
        assert (
            Solution.smallest_distance_pair(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
