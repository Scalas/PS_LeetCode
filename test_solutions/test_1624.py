import pytest
from solutions.sol_1624 import Solution

cases = [
    {
        "input": {
            "s": "aa",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "abca",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "cbzxy",
        },
        "output": -1,
    },
    {
        "input": {
            "s": "mgntdygtxrvxjnwksqhxuxtrv",
        },
        "output": 18,
    },
]


@pytest.mark.sol1624
def test_run():
    for case in cases:
        assert (
            Solution.max_length_between_equal_characters(
                s=case["input"]["s"],
            )
            == case["output"]
        )
