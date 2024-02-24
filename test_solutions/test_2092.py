import pytest
from solutions.sol_2092 import Solution

cases = [
    {
        "input": {
            "n": 6,
            "meetings": [[1, 2, 5], [2, 3, 8], [1, 5, 10]],
            "firstPerson": 1,
        },
        "output": [0, 1, 2, 3, 5],
    },
    {
        "input": {
            "n": 4,
            "meetings": [[3, 1, 3], [1, 2, 2], [0, 3, 3]],
            "firstPerson": 3,
        },
        "output": [0, 1, 3],
    },
    {
        "input": {
            "n": 5,
            "meetings": [[3, 4, 2], [1, 2, 1], [2, 3, 1]],
            "firstPerson": 1,
        },
        "output": [0, 1, 2, 3, 4],
    },
    {
        "input": {
            "n": 6,
            "meetings": [[0, 2, 1], [1, 3, 1], [4, 5, 1]],
            "firstPerson": 1,
        },
        "output": [0, 1, 2, 3],
    },
]


@pytest.mark.sol_2092
def test_run():
    for case in cases:
        assert (
            Solution.find_all_people(
                n=case["input"]["n"],
                meetings=case["input"]["meetings"],
                firstPerson=case["input"]["firstPerson"],
            )
            == case["output"]
        )
