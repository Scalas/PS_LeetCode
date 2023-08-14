import pytest
from solutions.sol_1751 import Solution

cases = [
    {
        "input": {
            "events": [[1, 2, 4], [3, 4, 3], [2, 3, 1]],
            "k": 2,
        },
        "output": 7,
    },
    {
        "input": {
            "events": [[1, 2, 4], [3, 4, 3], [2, 3, 10]],
            "k": 2,
        },
        "output": 10,
    },
    {
        "input": {
            "events": [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]],
            "k": 3,
        },
        "output": 9,
    },
]


@pytest.mark.sol_1751
def test_run():
    for case in cases:
        assert (
            Solution.max_value(
                events=case["input"]["events"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
