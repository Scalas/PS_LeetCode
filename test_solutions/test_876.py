import pytest

from converter.leet_code_utils import list_to_linked_list
from solutions.sol_876 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 3, 4, 5],
        },
        "output": 2,
    },
    {
        "input": {
            "head": [1, 2, 3, 4, 5, 6],
        },
        "output": 3,
    },
]


@pytest.mark.sol876
def test_run():
    for case in cases:
        linked_list = list_to_linked_list(case["input"]["head"])
        expected = linked_list
        for _ in range(case["output"]):
            expected = expected.next
        assert (
            Solution.middle_node(
                head=linked_list,
            )
            == expected
        )
