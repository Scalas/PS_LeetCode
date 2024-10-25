import pytest
from solutions.sol_1233 import Solution


cases = [
    {
        "input": {"folder": ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]},
        "output": ["/a", "/c/d", "/c/f"],
    },
    {
        "input": {"folder": ["/a", "/a/b/c", "/a/b/d"]},
        "output": ["/a"],
    },
    {
        "input": {"folder": ["/a/b/c", "/a/b/ca", "/a/b/d"]},
        "output": ["/a/b/c", "/a/b/ca", "/a/b/d"],
    },
]


@pytest.mark.sol1233
def test_run():
    for case in cases:
        assert sorted(
            Solution.remove_sub_folders(
                folder=case["input"]["folder"],
            )
        ) == sorted(case["output"])
