import pytest

from converter.leet_code_utils import (
    list_to_linked_list_with_random_pointer,
    compare_linked_list_with_random_pointer,
)
from solutions.sol_138 import Solution

cases = [
    {
        "input": {
            "head": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        },
        "output": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
    },
    {
        "input": {
            "head": [[1, 1], [2, 1]],
        },
        "output": [[1, 1], [2, 1]],
    },
    {
        "input": {
            "head": [[3, None], [3, 0], [3, None]],
        },
        "output": [[3, None], [3, 0], [3, None]],
    },
]


@pytest.mark.sol138
def test_run():
    for case in cases:
        head = list_to_linked_list_with_random_pointer(case["input"]["head"])
        assert compare_linked_list_with_random_pointer(
            Solution.copy_random_list(
                head=head,
            ),
            head,
        )
