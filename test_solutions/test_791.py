import pytest
from solutions.sol_791 import Solution

cases = [
    {"input": {"order": "cba", "s": "abcd"}, "output": "cbad"},
    {"input": {"order": "bcafg", "s": "abcd"}, "output": "bcad"},
]


@pytest.mark.sol_790
def test_run():
    for case in cases:
        assert (
            Solution.custom_sort_string(
                order=case["input"]["order"],
                s=case["input"]["s"],
            )
            == case["output"]
        )
