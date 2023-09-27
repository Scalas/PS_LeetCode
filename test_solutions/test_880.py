import pytest
from solutions.sol_880 import Solution

cases = [
    {
        "input": {
            "s": "leet2code3",
            "k": 10,
        },
        "output": "o",
    },
    {
        "input": {
            "s": "ha22",
            "k": 5,
        },
        "output": "h",
    },
    {
        "input": {
            "s": "a2345678999999999999999",
            "k": 1,
        },
        "output": "a",
    },
    {
        "input": {
            "s": "leet2code3",
            "k": 13,
        },
        "output": "l",
    },
]


@pytest.mark.sol880
def test_run():
    for case in cases:
        assert (
            Solution.decode_at_index(
                s=case["input"]["s"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
