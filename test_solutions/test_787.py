import pytest
from solutions.sol_787 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "flights": [
                [0, 1, 100],
                [1, 2, 100],
                [2, 0, 100],
                [1, 3, 600],
                [2, 3, 200],
            ],
            "src": 0,
            "dst": 3,
            "k": 1,
        },
        "output": 700,
    },
    {
        "input": {
            "n": 3,
            "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            "src": 0,
            "dst": 2,
            "k": 1,
        },
        "output": 200,
    },
    {
        "input": {
            "n": 3,
            "flights": [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            "src": 0,
            "dst": 2,
            "k": 0,
        },
        "output": 500,
    },
]


@pytest.mark.sol_787
def test_run():
    for case in cases:
        assert (
            Solution.find_cheapest_price(
                n=case["input"]["n"],
                flights=case["input"]["flights"],
                src=case["input"]["src"],
                dst=case["input"]["dst"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
