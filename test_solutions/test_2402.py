import pytest
from solutions.sol_2402 import Solution

cases = [
    {
        "input": {
            "n": 2,
            "meetings": [[0, 10], [1, 5], [2, 7], [3, 4]],
        },
        "output": 0,
    },
    {
        "input": {
            "n": 3,
            "meetings": [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]],
        },
        "output": 1,
    },
    {
        "input": {
            "n": 4,
            "meetings": [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]],
        },
        "output": 0,
    },
]


@pytest.mark.sol_2402
def test_run():
    for case in cases:
        assert (
            Solution.most_booked(
                n=case["input"]["n"],
                meetings=case["input"]["meetings"],
            )
            == case["output"]
        )
