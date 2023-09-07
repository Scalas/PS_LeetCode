import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_92 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 3, 4, 5],
            "left": 2,
            "right": 4
        },
        "output": [1, 4, 3, 2, 5],
    },
    {
        "input": {
            "head": [5],
            "left": 1,
            "right": 1
        },
        "output": [5]
    },
    {
        "input": {
            "head": [1, 2, 3],
            "left": 3,
            "right": 3
        },
        "output": [1, 2, 3]
    },
    {
        "input": {
            "head": [3, 5],
            "left": 1,
            "right": 2
        },
        "output": [5, 3]
    },
]


@pytest.mark.sol92
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.reverse_between(
                head=list_to_linked_list(case["input"]["head"]),
                left=case["input"]["left"],
                right=case["input"]["right"],
            ),
            list_to_linked_list(case["output"]),
        )
