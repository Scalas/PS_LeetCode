import pytest
from solutions.sol_1704 import Solution

cases = [
    {
        "input": {
            "s": "book",
        },
        "output": True,
    },
    {
        "input": {
            "s": "textbook",
        },
        "output": False,
    },
]


@pytest.mark.sol1704
def test_run():
    for case in cases:
        assert Solution.halves_are_alike(s=case["input"]["s"]) == case["output"]
