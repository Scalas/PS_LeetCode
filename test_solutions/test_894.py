import pytest

from converter.leet_code_utils import tree_to_list
from solutions.sol_894 import Solution

cases = [
    {
        "input": {
            "n": 7,
        },
        "output": [
            [0, 0, 0, None, None, 0, 0, None, None, 0, 0],
            [0, 0, 0, None, None, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
            [0, 0, 0, 0, 0, None, None, 0, 0],
        ],
    },
    {
        "input": {
            "n": 3,
        },
        "output": [[0, 0, 0]],
    },
]


@pytest.mark.sol894
def test_run():
    for case in cases:
        a = list(
            map(
                lambda x: tuple(tree_to_list(x)),
                Solution.all_possible_fbt(
                    n=case["input"]["n"],
                ),
            )
        )
        assert set(
            map(
                lambda x: tuple(tree_to_list(x)),
                Solution.all_possible_fbt(
                    n=case["input"]["n"],
                ),
            )
        ) == set(map(lambda x: tuple(x), case["output"]))
