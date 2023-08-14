import pytest
from solutions.sol_2390 import Solution

cases = [
    {
        "input": {
            "s": "leet**cod*e",
        },
        "output": "lecoe",
    },
    {
        "input": {
            "s": "erase*****",
        },
        "output": "",
    },
]


@pytest.mark.sol_2390
def test_run():
    for case in cases:
        assert (
            Solution.remove_stars(
                s=case["input"]["s"],
            )
            == case["output"]
        )
