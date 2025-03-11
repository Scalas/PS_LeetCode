import pytest
from solutions.sol_1358 import Solution


cases = [
    {
        "input": {"s": "abcabc"},
        "output": 10,
    },
    {
        "input": {"s": "aaacb"},
        "output": 3,
    },
    {
        "input": {"s": "abc"},
        "output": 1,
    },
]


@pytest.mark.sol1358
def test_run():
    for case in cases:
        assert (
            Solution.number_of_substrings(
                s=case["input"]["s"],
            )
            == case["output"]
        )
