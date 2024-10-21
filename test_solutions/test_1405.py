import pytest
from solutions.sol_1405 import Solution


cases = [
    {
        "input": {"a": 1, "b": 1, "c": 7},
        "output": "ccaccbcc",
    },
    {
        "input": {"a": 7, "b": 1, "c": 0},
        "output": "aabaa",
    },
]


@pytest.mark.sol1405
def test_run():
    for case in cases:
        assert (
            Solution.longest_diverse_string(
                a=case["input"]["a"],
                b=case["input"]["b"],
                c=case["input"]["c"],
            )
            == case["output"]
        )
