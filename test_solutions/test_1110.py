import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_1110 import Solution


cases = [
    {
        "input": {"root": [1, 2, 3, 4, 5, 6, 7], "to_delete": [3, 5]},
        "output": [[1, 2, None, 4], [6], [7]],
    },
    {
        "input": {"root": [1, 2, 4, None, 3], "to_delete": [3]},
        "output": [[1, 2, 4]],
    },
]


@pytest.mark.sol1110
def test_run():
    for case in cases:
        forests = Solution.del_nodes(
            to_delete=case["input"]["to_delete"],
            root=list_to_tree(case["input"]["root"]),
        )
        for root1, root2 in zip(forests, map(list_to_tree, case["output"])):
            assert compare_tree(root1, root2)
