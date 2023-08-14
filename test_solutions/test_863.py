import pytest
from solutions.sol_863 import Solution
from converter.leet_code_utils import list_to_tree, find_from_tree

cases = [
    {
        "input": {"root": [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], "target": 5, "k": 2},
        "output": [7, 4, 1],
    },
    {
        "input": {"root": [1], "target": 1, "k": 3},
        "output": [],
    },
]


@pytest.mark.sol_863
def test_run():
    for case in cases:
        root = list_to_tree(case["input"]["root"])
        target = find_from_tree(root, case["input"]["target"])

        assert set(
            Solution.distance_k(
                root=root,
                target=target,
                k=case["input"]["k"],
            )
        ) == set(case["output"])
