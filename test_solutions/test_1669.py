import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_1669 import Solution

cases = [
    {
        "input": {
            "list1": [10, 1, 13, 6, 9, 5],
            "a": 3,
            "b": 4,
            "list2": [1000000, 1000001, 1000002],
        },
        "output": [10, 1, 13, 1000000, 1000001, 1000002, 5],
    },
    {
        "input": {
            "list1": [0, 1, 2, 3, 4, 5, 6],
            "a": 2,
            "b": 5,
            "list2": [1000000, 1000001, 1000002, 1000003, 1000004],
        },
        "output": [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6],
    },
]


@pytest.mark.sol_1669
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.merge_in_between(
                list1=list_to_linked_list(case["input"]["list1"]),
                a=case["input"]["a"],
                b=case["input"]["b"],
                list2=list_to_linked_list(case["input"]["list2"]),
            ),
            list_to_linked_list(case["output"]),
        )
