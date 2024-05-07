import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_2816 import Solution

cases = [
    {
        "input": {
            "head": [1, 8, 9],
        },
        "output": [3, 7, 8],
    },
    {
        "input": {
            "head": [9, 9, 9],
        },
        "output": [1, 9, 9, 8],
    },
]


@pytest.mark.sol_2816
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.double_it(head=list_to_linked_list(case["input"]["head"])),
            list_to_linked_list(case["output"]),
        )
