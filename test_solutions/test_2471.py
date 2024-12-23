import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2471 import Solution


cases = [
    {
        "input": {"root": [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]},
        "output": 3,
    },
    {
        "input": {"root": [1, 3, 2, 7, 6, 5, 4]},
        "output": 3,
    },
    {
        "input": {"root": [1, 2, 3, 4, 5, 6]},
        "output": 0,
    },
]


@pytest.mark.sol2471
def test_run():
    for case in cases:
        assert (
            Solution.minimum_operations(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
