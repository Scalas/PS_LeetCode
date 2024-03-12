import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_1171 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, -3, 3, 1],
        },
        "output": [3, 1],
    },
    {
        "input": {
            "head": [1, 2, 3, -3, 4],
        },
        "output": [1, 2, 4],
    },
    {
        "input": {
            "head": [1, 2, 3, -3, -2],
        },
        "output": [1],
    },
]


@pytest.mark.sol_1171
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.remove_zero_sum_sub_lists(
                head=list_to_linked_list(case["input"]["head"]),
            ),
            list_to_linked_list(case["output"]),
        )
