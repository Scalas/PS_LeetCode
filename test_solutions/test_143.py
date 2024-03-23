import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_143 import Solution

cases = [
    {"input": {"head": [1, 2, 3, 4]}, "output": [1, 4, 2, 3]},
    {"input": {"head": [1, 2, 3, 4, 5]}, "output": [1, 5, 2, 4, 3]},
]


@pytest.mark.sol143
def test_run():
    for case in cases:
        head = list_to_linked_list(case["input"]["head"])
        Solution.reorder_list(
            head=head,
        )
        assert compare_linked_list(head, list_to_linked_list(case["output"]))
