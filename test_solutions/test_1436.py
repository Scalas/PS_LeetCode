import pytest
from solutions.sol_1436 import Solution

cases = [
    {
        "input": {
            "paths": [
                ["London", "New York"],
                ["New York", "Lima"],
                ["Lima", "Sao Paulo"],
            ],
        },
        "output": "Sao Paulo",
    },
    {
        "input": {
            "paths": [["B", "C"], ["D", "B"], ["C", "A"]],
        },
        "output": "A",
    },
    {
        "input": {
            "paths": [["A", "Z"]],
        },
        "output": "Z",
    },
]


@pytest.mark.sol1436
def test_run():
    for case in cases:
        assert (
            Solution.dest_city(
                paths=case["input"]["paths"],
            )
            == case["output"]
        )
