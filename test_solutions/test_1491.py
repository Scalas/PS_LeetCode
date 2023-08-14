import pytest
from solutions.sol_1491 import Solution

cases = [
    {
        "input": {
            "salary": [4000, 3000, 1000, 2000],
        },
        "output": 2500.00000,
    },
    {
        "input": {
            "salary": [1000, 2000, 3000],
        },
        "output": 2000.00000,
    },
    {
        "input": {
            "salary": [
                48000,
                59000,
                99000,
                13000,
                78000,
                45000,
                31000,
                17000,
                39000,
                37000,
                93000,
                77000,
                33000,
                28000,
                4000,
                54000,
                67000,
                6000,
                1000,
                11000,
            ],
        },
        "output": 41111.11111,
    },
]


@pytest.mark.sol1491
def test_run():
    for case in cases:
        assert (
            round(
                Solution.average(
                    salary=case["input"]["salary"],
                ),
                5,
            )
            == case["output"]
        )
