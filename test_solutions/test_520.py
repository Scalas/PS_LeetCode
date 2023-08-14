import pytest
from solutions.sol_520 import Solution

cases = [
    {"input": {"word": "USA"}, "output": True},
    {"input": {"word": "FFFFf"}, "output": False},
    {"input": {"word": "train"}, "output": True},
    {"input": {"word": "gOlF"}, "output": False},
]


@pytest.mark.sol_520
def test_run():
    for case in cases:
        assert Solution.detect_capital_use(word=case["input"]["word"]) == case["output"]
