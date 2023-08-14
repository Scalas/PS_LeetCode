import pytest
from solutions.sol_2466 import Solution

cases = [
    {
        "input": {
            "low": 3,
            "high": 3,
            "zero": 1,
            "one": 1,
        },
        "output": 8,
    },
    {
        "input": {
            "low": 2,
            "high": 3,
            "zero": 1,
            "one": 2,
        },
        "output": 5,
    },
]


@pytest.mark.sol_2466
def test_run():
    for case in cases:
        assert (
            Solution.count_good_strings(
                low=case["input"]["low"],
                high=case["input"]["high"],
                zero=case["input"]["zero"],
                one=case["input"]["one"],
            )
            == case["output"]
        )
