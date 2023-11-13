import pytest
from solutions.sol_2785 import Solution

cases = [
    {
        "input": {
            "s": "lEetcOde",
        },
        "output": "lEOtcede",
    },
    {
        "input": {
            "s": "lYmpH",
        },
        "output": "lYmpH",
    },
]


@pytest.mark.sol_2785
def test_run():
    for case in cases:
        assert Solution.sort_vowels(s=case["input"]["s"]) == case["output"]
