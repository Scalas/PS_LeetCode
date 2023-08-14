import pytest

from converter.leet_code_utils import tree_to_list
from solutions.sol_95 import Solution

cases = [
    {
        "input": {
            "n": 3,
        },
        "output": [
            [1, None, 2, None, 3],
            [1, None, 3, 2],
            [2, 1, 3],
            [3, 1, None, None, 2],
            [3, 2, None, 1],
        ],
    },
    {
        "input": {
            "n": 1,
        },
        "output": [[1]],
    },
]


@pytest.mark.sol95
def test_run():
    for case in cases:
        assert set(
            map(
                lambda x: tuple(tree_to_list(x)),
                Solution.generate_trees(n=case["input"]["n"]),
            )
        ) == set(map(tuple, case["output"]))
