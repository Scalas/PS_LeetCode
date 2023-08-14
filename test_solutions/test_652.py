import pytest
from solutions.sol_652 import Solution
from converter.leet_code_utils import list_to_tree, compare_tree

cases = [
    {
        "input": {
            "root": [1, 2, 3, 4, None, 2, 4, None, None, 4],
        },
        "output": [[2, 4], [4]],
    },
    {
        "input": {
            "root": [2, 1, 1],
        },
        "output": [[1]],
    },
    {
        "input": {
            "root": [2, 2, 2, 3, None, 3, None],
        },
        "output": [[2, 3], [3]],
    },
]


@pytest.mark.sol_652
def test_run():
    for case in cases:
        result = Solution.find_duplicate_subtrees(
            root=list_to_tree(case["input"]["root"]),
        )
        expected = list(map(list_to_tree, case["output"]))
        for sub_tree in result:
            check = False
            for cand in expected:
                if compare_tree(sub_tree, cand):
                    check = True
                    break
            assert check is True
