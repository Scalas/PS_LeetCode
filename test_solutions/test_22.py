import pytest

from solutions.sol_22 import Solution

cases = [
    {
        "input": {
            "n": 3,
        },
        "output": ["((()))", "(()())", "(())()", "()(())", "()()()"],
    },
    {
        "input": {
            "n": 1,
        },
        "output": ["()"],
    },
]


@pytest.mark.sol22
def test_run():
    for case in cases:
        assert (
            Solution.generate_parenthesis(
                n=case["input"]["n"],
            )
            == case["output"]
        )
