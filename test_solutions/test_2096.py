import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2096 import Solution


cases = [
    {
        "input": {"root": [5, 1, 2, 3, None, 6, 4], "startValue": 3, "destValue": 6},
        "output": "UURL",
    },
    {
        "input": {"root": [2, 1], "startValue": 2, "destValue": 1},
        "output": "L",
    },
]


@pytest.mark.sol2096
def test_run():
    for case in cases:
        assert (
            Solution.get_directions(
                startValue=case["input"]["startValue"],
                root=list_to_tree(case["input"]["root"]),
                destValue=case["input"]["destValue"],
            )
            == case["output"]
        )
