import pytest
from solutions.sol_402 import Solution

cases = [
    {
        "input": {
            "num": "1432219",
            "k": 3,
        },
        "output": "1219",
    },
    {
        "input": {
            "num": "10200",
            "k": 1,
        },
        "output": "200",
    },
    {
        "input": {
            "num": "10",
            "k": 2,
        },
        "output": "0",
    },
    {
        "input": {
            "num": "10",
            "k": 1,
        },
        "output": "0",
    },
    {
        "input": {
            "num": "112",
            "k": 1,
        },
        "output": "11",
    },
    {
        "input": {
            "num": "1234567890",
            "k": 9,
        },
        "output": "0",
    },
]


@pytest.mark.sol402
def test_run():
    for case in cases:
        assert (
            Solution.remove_k_digits(
                num=case["input"]["num"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
