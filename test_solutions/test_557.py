import pytest
from solutions.sol_557 import Solution

cases = [
    {
        "input": {
            "s": "Let's take LeetCode contest",
        },
        "output": "s'teL ekat edoCteeL tsetnoc",
    },
    {
        "input": {
            "s": "God Ding",
        },
        "output": "doG gniD",
    },
]


@pytest.mark.sol_557
def test_run():
    for case in cases:
        assert Solution.reverse_words(s=case["input"]["s"]) == case["output"]
