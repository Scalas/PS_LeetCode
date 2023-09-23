import pytest
from solutions.sol_1048 import Solution

cases = [
    {
        "input": {
            "words": ["a", "b", "ba", "bca", "bda", "bdca"],
        },
        "output": 4,
    },
    {
        "input": {
            "words": ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"],
        },
        "output": 5,
    },
    {
        "input": {
            "words": ["abcd", "dbqca"],
        },
        "output": 1,
    },
]


@pytest.mark.sol1048
def test_run():
    for case in cases:
        assert (
            Solution.longest_str_chain(
                words=case["input"]["words"],
            )
            == case["output"]
        )
