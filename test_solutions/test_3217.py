import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_3217 import Solution


cases = [
    {
        "input": {"nums": [1, 2, 3], "head": list_to_linked_list([1, 2, 3, 4, 5])},
        "output": [4, 5],
    },
    {
        "input": {"nums": [1], "head": list_to_linked_list([1, 2, 1, 2, 1, 2])},
        "output": [2, 2, 2],
    },
    {
        "input": {"nums": [5], "head": list_to_linked_list([1, 2, 3, 4])},
        "output": [1, 2, 3, 4],
    },
]


@pytest.mark.sol3217
def test_run():
    for case in cases:
        assert compare_linked_list(
            Solution.modified_list(
                head=case["input"]["head"],
                nums=case["input"]["nums"],
            ),
            list_to_linked_list(case["output"]),
        )
