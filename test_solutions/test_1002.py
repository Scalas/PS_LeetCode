import pytest
from solutions.sol_1002 import Solution

cases = [
    {"input": {"words": ["bella", "label", "roller"]}, "output": ["e", "l", "l"]},
    {"input": {"words": ["cool", "lock", "cook"]}, "output": ["c", "o"]},
]


@pytest.mark.sol1002
def test_run():
    for case in cases:
        assert Solution.common_chars(words=case["input"]["words"]) == case["output"]
