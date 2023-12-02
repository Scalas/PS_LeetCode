import pytest
from solutions.sol_1160 import Solution

cases = [
    {"input": {"words": ["cat", "bt", "hat", "tree"], "chars": "atach"}, "output": 6},
    {
        "input": {"words": ["hello", "world", "leetcode"], "chars": "welldonehoneyr"},
        "output": 10,
    },
]


@pytest.mark.sol1160
def test_run():
    for case in cases:
        assert (
            Solution.count_characters(
                words=case["input"]["words"], chars=case["input"]["chars"]
            )
            == case["output"]
        )
