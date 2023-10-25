import pytest
from solutions.sol_779 import Solution

cases = [
    {
        "input": {
            "n": 2,
            "k": 1,
        },
        "output": 0,
    },
    {
        "input": {
            "n": 1,
            "k": 1,
        },
        "output": 0,
    },
    {
        "input": {
            "n": 2,
            "k": 2,
        },
        "output": 1,
    },
]


@pytest.mark.sol_779
def test_run():
    for case in cases:
        assert (
            Solution.kth_grammar(
                n=case["input"]["n"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
