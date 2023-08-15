import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_86 import Solution

cases = [
    {
        "input": {
            "head": [1, 4, 3, 2, 5, 2],
            "x": 3,
        },
        "output": [1, 2, 2, 4, 3, 5],
    },
    {
        "input": {
            "head": [2, 1],
            "x": 2,
        },
        "output": [1, 2],
    },
    {
        "input": {
            "head": [1],
            "x": 0,
        },
        "output": [1],
    },
    {
        "input": {
            "head": [1],
            "x": 2,
        },
        "output": [1],
    },
]


@pytest.mark.sol86
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.partition(
                head=list_to_linked_list(case["input"]["head"]),
                x=case["input"]["x"],
            ),
            list_to_linked_list(case["output"]),
        )
