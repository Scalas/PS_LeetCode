import pytest
from solutions.sol_131 import Solution

cases = [
    {"input": {"s": "aab"}, "output": [["a", "a", "b"], ["aa", "b"]]},
    {"input": {"s": "a"}, "output": [["a"]]},
]


@pytest.mark.sol131
def test_run():
    for case in cases:
        assert Solution.partition(s=case["input"]["s"]) == case["output"]
