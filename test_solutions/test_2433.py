import pytest
from solutions.sol_2433 import Solution

cases = [
    {
        "input": {
            "pref": [5, 2, 0, 3, 1],
        },
        "output": [5, 7, 2, 3, 2],
    },
    {
        "input": {
            "pref": [13],
        },
        "output": [13],
    },
]


@pytest.mark.sol_2433
def test_run():
    for case in cases:
        assert (
            Solution.find_array(
                pref=case["input"]["pref"],
            )
            == case["output"]
        )
