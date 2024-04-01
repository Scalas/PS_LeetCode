import pytest
from solutions.sol_58 import Solution

cases = [
    {
        "input": {
            "s": "Hello World",
        },
        "output": 5,
    },
    {
        "input": {
            "s": "   fly me   to   the moon  ",
        },
        "output": 4,
    },
    {
        "input": {
            "s": "luffy is still joyboy",
        },
        "output": 6,
    },
]


@pytest.mark.sol58
def test_run():
    for case in cases:
        assert (
            Solution.length_of_last_word(
                s=case["input"]["s"],
            )
            == case["output"]
        )
