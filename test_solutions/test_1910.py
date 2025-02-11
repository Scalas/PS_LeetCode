import pytest
from solutions.sol_1910 import Solution


cases = [
    {
        "input": {"s": "daabcbaabcbc", "part": "abc"},
        "output": "dab",
    },
    {
        "input": {"s": "axxxxyyyyb", "part": "xy"},
        "output": "ab",
    },
]


@pytest.mark.sol1910
def test_run():
    for case in cases:
        assert (
            Solution.remove_occurrences(
                part=case["input"]["part"],
                s=case["input"]["s"],
            )
            == case["output"]
        )
