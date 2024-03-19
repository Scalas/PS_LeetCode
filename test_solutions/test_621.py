import pytest

from solutions.sol_621 import Solution

cases = [
    {"input": {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2}, "output": 8},
    {"input": {"tasks": ["A", "C", "A", "B", "D", "B"], "n": 1}, "output": 6},
    {"input": {"tasks": ["A", "A", "A", "B", "B", "B"], "n": 3}, "output": 10},
    {
        "input": {
            "tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            "n": 1,
        },
        "output": 12,
    },
]


@pytest.mark.sol_621
def test_run():
    for case in cases:
        assert (
            Solution.least_interval(
                tasks=case["input"]["tasks"],
                n=case["input"]["n"],
            )
            == case["output"]
        )
