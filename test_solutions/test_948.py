import pytest
from solutions.sol_948 import Solution

cases = [
    {
        "input": {
            "tokens": [100],
            "power": 50,
        },
        "output": 0,
    },
    {
        "input": {
            "tokens": [200, 100],
            "power": 150,
        },
        "output": 1,
    },
    {
        "input": {
            "tokens": [100, 200, 300, 400],
            "power": 200,
        },
        "output": 2,
    },
    {
        "input": {
            "tokens": [71, 55, 82],
            "power": 54,
        },
        "output": 0,
    },
]


@pytest.mark.sol946
def test_run():
    for case in cases:
        assert (
            Solution.bag_of_tokens_score(
                tokens=case["input"]["tokens"], power=case["input"]["power"]
            )
            == case["output"]
        )
