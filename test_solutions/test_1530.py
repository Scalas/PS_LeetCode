import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_1530 import Solution


cases = [
    {
        "input": {"root": [1, 2, 3, None, 4], "distance": 3},
        "output": 1,
    },
    {
        "input": {"root": [1, 2, 3, 4, 5, 6, 7], "distance": 3},
        "output": 2,
    },
    {
        "input": {
            "root": [7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2],
            "distance": 3,
        },
        "output": 1,
    },
    {
        "input": {"root": [1, 1, 1], "distance": 2},
        "output": 1,
    },
    {
        "input": {
            "root": [
                15,
                66,
                55,
                97,
                60,
                12,
                56,
                None,
                54,
                None,
                49,
                None,
                9,
                None,
                None,
                None,
                None,
                None,
                90,
            ],
            "distance": 5,
        },
        "output": 3,
    },
]


@pytest.mark.sol1530
def test_run():
    for case in cases:
        assert (
            Solution.count_pairs(
                distance=case["input"]["distance"],
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
