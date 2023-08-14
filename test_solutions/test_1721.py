import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_1721 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 3, 4, 5],
            "k": 2,
        },
        "output": [1, 4, 3, 2, 5],
    },
    {
        "input": {
            "head": [7, 9, 6, 6, 7, 8, 3, 0, 9, 5],
            "k": 5,
        },
        "output": [7, 9, 6, 6, 8, 7, 3, 0, 9, 5],
    },
    {
        "input": {
            "head": [1, 2],
            "k": 1,
        },
        "output": [2, 1],
    },
    {
        "input": {
            "head": [4, 1, 2, 5],
            "k": 2,
        },
        "output": [4, 2, 1, 5],
    },
]


@pytest.mark.sol1721
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.swap_nodes(
                head=list_to_linked_list(case["input"]["head"]),
                k=case["input"]["k"],
            ),
            list_to_linked_list(case["output"]),
        )
