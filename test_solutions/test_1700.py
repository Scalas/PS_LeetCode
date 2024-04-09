import pytest
from solutions.sol_1700 import Solution

cases = [
    {
        "input": {
            "students": [1, 1, 0, 0],
            "sandwiches": [0, 1, 0, 1],
        },
        "output": 0,
    },
    {
        "input": {
            "students": [1, 1, 1, 0, 0, 1],
            "sandwiches": [1, 0, 0, 0, 1, 1],
        },
        "output": 3,
    },
]


@pytest.mark.sol1700
def test_run():
    for case in cases:
        assert (
            Solution.count_students(
                students=case["input"]["students"],
                sandwiches=case["input"]["sandwiches"],
            )
            == case["output"]
        )
