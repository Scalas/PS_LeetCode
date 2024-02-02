import pytest
from solutions.sol_1291 import Solution

cases = [
    {
        "input": {
            "low": 100,
            "high": 300,
        },
        "output": [123, 234],
    },
    {
        "input": {
            "low": 1000,
            "high": 13000,
        },
        "output": [1234, 2345, 3456, 4567, 5678, 6789, 12345],
    },
]


@pytest.mark.sol1291
def test_run():
    for case in cases:
        assert (
            Solution.sequential_digits(
                low=case["input"]["low"],
                high=case["input"]["high"],
            )
            == case["output"]
        )
