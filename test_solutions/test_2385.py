import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2385 import Solution

cases = [
    {
        "input": {
            "root": [1, 5, 3, None, 4, 10, 6, 9, 2],
            "start": 3,
        },
        "output": 4,
    },
    {
        "input": {
            "root": [1],
            "start": 1,
        },
        "output": 0,
    },
]


@pytest.mark.sol2385
def test_run():
    for case in cases:
        assert (
            Solution.amount_of_time(
                root=list_to_tree(case["input"]["root"]),
                start=case["input"]["start"],
            )
            == case["output"]
        )
