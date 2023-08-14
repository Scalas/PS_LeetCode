import pytest

from converter.leet_code_utils import list_to_linked_list
from solutions.sol_2130 import Solution

cases = [
    {
        "input": {
            "head": [5, 4, 2, 1],
        },
        "output": 6,
    },
    {
        "input": {
            "head": [4, 2, 2, 3],
        },
        "output": 7,
    },
    {
        "input": {
            "head": [1, 100000],
        },
        "output": 100001,
    },
]


@pytest.mark.sol_2130
def test_run():
    for case in cases:
        assert (
            Solution.pair_sum(
                head=list_to_linked_list(case["input"]["head"]),
            )
            == case["output"]
        )
