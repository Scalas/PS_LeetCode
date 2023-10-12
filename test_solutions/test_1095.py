import pytest

from leet_code_types.leet_code_types import MountainArray
from solutions.sol_1095 import Solution

cases = [
    {
        "input": {"array": [1, 2, 3, 4, 5, 3, 1], "target": 3},
        "output": 2,
    },
    {
        "input": {"array": [0, 1, 2, 4, 2, 1], "target": 3},
        "output": -1,
    },
    {
        "input": {"array": [1, 5, 2], "target": 2},
        "output": 2,
    },
]


@pytest.mark.sol1095
def test_run():
    for case in cases:
        assert (
            Solution.find_in_mountain_array(
                target=case["input"]["target"],
                mountain_arr=MountainArray(case["input"]["array"]),
            )
            == case["output"]
        )
