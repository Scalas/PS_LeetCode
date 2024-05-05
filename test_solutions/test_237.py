import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_237 import Solution

cases = [
    {
        "input": {"head": [4, 5, 1, 9], "node": 5},
        "output": [4, 1, 9],
    },
    {
        "input": {"head": [4, 5, 1, 9], "node": 1},
        "output": [4, 5, 9],
    },
]


@pytest.mark.sol237
def test_run():
    for case in cases:
        head = list_to_linked_list(case["input"]["head"])
        node = head
        while node.val != case["input"]["node"]:
            node = node.next
        expected = list_to_linked_list(case["output"])

        Solution.delete_node(
            node=node,
        )
        assert compare_linked_list(head, expected)
