import pytest
from solutions.sol_1422 import Solution

cases = [
    {
        "input": {
            "s": "011101",
        },
        "output": 5,
    },
    {
        "input": {
            "s": "00111",
        },
        "output": 5,
    },
    {
        "input": {
            "s": "1111",
        },
        "output": 3,
    },
]


@pytest.mark.sol1422
def test_run():
    for case in cases:
        assert (
            Solution.max_score(
                s=case["input"]["s"],
            )
            == case["output"]
        )
