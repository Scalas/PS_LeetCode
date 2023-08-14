import pytest
from solutions.sol_100 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {"input": {"p": [1, 2, 3], "q": [1, 2, 3]}, "output": True},
    {"input": {"p": [1, 2], "q": [1, None, 2]}, "output": False},
    {"input": {"p": [1, 2, 1], "q": [1, 1, 2]}, "output": False},
]


@pytest.mark.sol100
def test_run():
    for case in cases:
        assert (
            Solution.is_same_tree(
                p=list_to_tree(case["input"]["p"]), q=list_to_tree(case["input"]["q"])
            )
            == case["output"]
        )
