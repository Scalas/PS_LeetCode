import pytest
from solutions.sol_2108 import Solution

cases = [
    {
        "input": {
            "words": ["abc", "car", "ada", "racecar", "cool"],
        },
        "output": "ada",
    },
    {
        "input": {
            "words": ["notapalindrome", "racecar"],
        },
        "output": "racecar",
    },
    {
        "input": {
            "words": ["def", "ghi"],
        },
        "output": "",
    },
]


@pytest.mark.sol_2108
def test_run():
    for case in cases:
        assert (
            Solution.first_palindrome(
                words=case["input"]["words"],
            )
            == case["output"]
        )
