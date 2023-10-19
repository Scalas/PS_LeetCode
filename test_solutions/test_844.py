import pytest
from solutions.sol_844 import Solution

cases = [
    {"input": {"s": "ab#c", "t": "ad#c"}, "output": True},
    {"input": {"s": "ab##", "t": "c#d#"}, "output": True},
    {"input": {"s": "a#c", "t": "b"}, "output": False},
]


@pytest.mark.sol844
def test_run():
    for case in cases:
        assert (
            Solution.backspace_compare(s=case["input"]["s"], t=case["input"]["t"])
            == case["output"]
        )
