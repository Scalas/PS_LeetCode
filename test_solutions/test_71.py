import pytest
from solutions.sol_71 import Solution

cases = [
    {
        "input": {
            "path": "/home/",
        },
        "output": "/home",
    },
    {
        "input": {
            "path": "/../",
        },
        "output": "/",
    },
    {
        "input": {
            "path": "/../",
        },
        "output": "/",
    },
]


@pytest.mark.sol71
def test_run():
    for case in cases:
        assert Solution.simplify_path(path=case["input"]["path"]) == case["output"]
