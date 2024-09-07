import pytest

from converter.leet_code_utils import list_to_linked_list, list_to_tree
from solutions.sol_1367 import Solution


cases = [
    {
        "input": {
            "head": [4, 2, 8],
            "root": [
                1,
                4,
                4,
                None,
                2,
                2,
                None,
                1,
                None,
                6,
                8,
                None,
                None,
                None,
                None,
                1,
                3,
            ],
        },
        "output": True,
    },
    {
        "input": {
            "head": [1, 4, 2, 6],
            "root": [
                1,
                4,
                4,
                None,
                2,
                2,
                None,
                1,
                None,
                6,
                8,
                None,
                None,
                None,
                None,
                1,
                3,
            ],
        },
        "output": True,
    },
    {
        "input": {
            "head": [1, 4, 2, 6, 8],
            "root": [
                1,
                4,
                4,
                None,
                2,
                2,
                None,
                1,
                None,
                6,
                8,
                None,
                None,
                None,
                None,
                1,
                3,
            ],
        },
        "output": False,
    },
]


@pytest.mark.sol1367
def test_run():
    for case in cases:
        assert (
            Solution.is_sub_path(
                root=list_to_tree(case["input"]["root"]),
                head=list_to_linked_list(case["input"]["head"]),
            )
            == case["output"]
        )
