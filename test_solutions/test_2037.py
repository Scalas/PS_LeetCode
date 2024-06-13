import pytest
from solutions.sol_2037 import Solution

cases = [
    {
        "input": {
            "seats": [3, 1, 5],
            "students": [2, 7, 4],
        },
        "output": 4,
    },
    {
        "input": {
            "seats": [4, 1, 5, 9],
            "students": [1, 3, 2, 6],
        },
        "output": 7,
    },
    {
        "input": {
            "seats": [
                2,
                2,
                6,
                6,
            ],
            "students": [1, 3, 2, 6],
        },
        "output": 4,
    },
]


@pytest.mark.sol_2037
def test_run():
    for case in cases:
        assert (
            Solution.min_moves_to_seat(
                seats=case["input"]["seats"],
                students=case["input"]["students"],
            )
            == case["output"]
        )
