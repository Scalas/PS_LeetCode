import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_1261 import FindElements


cases = [
    {
        "input": {
            "commands": [
                "FindElements",
                "find",
                "find",
            ],
            "args": [[-1, None, -1], [1], [2]],
        },
        "output": [None, False, True],
    }
]


@pytest.mark.sol1261
def test_run():
    for case in cases:
        args = case["input"]["args"]
        fe = FindElements(list_to_tree(args[0]))
        res = [None]
        for arg in args[1:]:
            res.append(fe.find(arg[0]))
        assert res == case["output"]
