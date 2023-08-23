import pytest
from solutions.sol_767 import Solution

cases = [
    {"input": {"s": "aab"}, "output": "aba"},
    {"input": {"s": "aaab"}, "output": ""},
    {"input": {"s": "vvvlo"}, "output": "vlvov"},
]


@pytest.mark.sol_767
def test_run():
    for case in cases:
        assert (
                Solution.reorganize_string(
                    s=case["input"]["s"],
                )
                == case["output"]
        )
