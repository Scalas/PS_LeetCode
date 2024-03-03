import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_19 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 3, 4, 5],
            "n": 2,
        },
        "output": [1, 2, 3, 5],
    },
    {
        "input": {
            "head": [1],
            "n": 1,
        },
        "output": [],
    },
    {
        "input": {
            "head": [1, 2],
            "n": 1,
        },
        "output": [1],
    },
]


@pytest.mark.sol19
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.remove_nth_from_end(
                head=list_to_linked_list(case["input"]["head"]),
                n=case["input"]["n"],
            ),
            list_to_linked_list(case["output"]),
        )
