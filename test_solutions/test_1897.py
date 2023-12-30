import pytest
from solutions.sol_1897 import Solution

cases = [
    {
        "input": {
            "words": ["abc", "aabc", "bc"],
        },
        "output": True,
    },
    {
        "input": {
            "words": ["ab", "a"],
        },
        "output": False,
    },
]


@pytest.mark.sol1897
def test_run():
    for case in cases:
        assert (
            Solution.make_equal(
                words=case["input"]["words"],
            )
            == case["output"]
        )
