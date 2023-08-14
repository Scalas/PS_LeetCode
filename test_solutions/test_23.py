import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_23 import Solution

cases = [
    {
        "input": {
            "lists": [[1, 4, 5], [1, 3, 4], [2, 6]],
        },
        "output": [1, 1, 2, 3, 4, 4, 5, 6],
    },
    {
        "input": {
            "lists": [],
        },
        "output": [],
    },
    {
        "input": {
            "lists": [[]],
        },
        "output": [],
    },
]


@pytest.mark.sol18
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.merge_k_lists(
                lists=list(map(list_to_linked_list, case["input"]["lists"])),
            ),
            list_to_linked_list(case["output"]),
        )
