import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_24 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 3, 4],
        },
        "output": [2, 1, 4, 3],
    },
    {
        "input": {
            "head": [],
        },
        "output": [],
    },
    {
        "input": {
            "head": [1],
        },
        "output": [1],
    },
]


@pytest.mark.sol24
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.swap_pairs(
                head=list_to_linked_list(case["input"]["head"]),
            ),
            list_to_linked_list(case["output"]),
        )
