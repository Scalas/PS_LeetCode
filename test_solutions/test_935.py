import pytest
from solutions.sol_935 import Solution

cases = [
    {
        "input": {
            "n": 1,
        },
        "output": 10,
    },
    {
        "input": {
            "n": 2,
        },
        "output": 20,
    },
    {
        "input": {
            "n": 3131,
        },
        "output": 136006598,
    },
]


@pytest.mark.sol935
def test_run():
    for case in cases:
        assert Solution.knight_dialer(n=case["input"]["n"]) == case["output"]
