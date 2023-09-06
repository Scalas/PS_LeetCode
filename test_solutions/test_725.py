import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_725 import Solution

cases = [
    {
        "input": {"head": [1, 2, 3], "k": 5},
        "output": [[1], [2], [3], [], []],
    },
    {
        "input": {"head": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "k": 3},
        "output": [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]],
    },
]


@pytest.mark.sol_725
def test_run():
    for case in cases:
        slots = Solution.split_list_to_parts(
            head=list_to_linked_list(case["input"]["head"]),
            k=case["input"]["k"],
        )
        expected = list(map(list_to_linked_list, case["output"]))
        for i in range(len(expected)):
            assert compare_linked_list(slots[i], expected[i])
