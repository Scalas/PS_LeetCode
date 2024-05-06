import pytest

from converter.leet_code_utils import compare_linked_list, list_to_linked_list
from solutions.sol_2487 import Solution

cases = [
    {"input": {"head": [5, 2, 13, 3, 8]}, "output": [13, 8]},
    {"input": {"head": [1, 1, 1, 1]}, "output": [1, 1, 1, 1]},
]


@pytest.mark.sol_2487
def test_run():
    for case in cases:
        head = list_to_linked_list(case["input"]["head"])
        actual = Solution.remove_nodes(head=head)
        expected = list_to_linked_list(case["output"])
        assert compare_linked_list(actual, expected)
