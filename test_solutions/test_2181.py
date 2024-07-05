import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_2181 import Solution


cases = [
    {
        "input": {"head": [0, 3, 1, 0, 4, 5, 2, 0]},
        "output": [4, 11],
    },
    {
        "input": {"head": [0, 1, 0, 3, 0, 2, 2, 0]},
        "output": [1, 3, 4],
    },
]


@pytest.mark.sol2181
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.merge_nodes(
                head=list_to_linked_list(case["input"]["head"]),
            ),
            list_to_linked_list(case["output"]),
        )
