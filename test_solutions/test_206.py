import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_206 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 3, 4, 5],
        },
        "output": [5, 4, 3, 2, 1],
    },
    {
        "input": {
            "head": [1, 2],
        },
        "output": [2, 1],
    },
]


@pytest.mark.sol206
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.reverse_list(
                head=list_to_linked_list(case["input"]["head"]),
            ),
            list_to_linked_list(case["output"]),
        )
