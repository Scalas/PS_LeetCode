import pytest
from solutions.sol_857 import Solution

cases = [
    {
        "input": {"quality": [10, 20, 5], "wage": [70, 50, 30], "k": 2},
        "output": 105.00000,
    },
    {
        "input": {"quality": [3, 1, 10, 10, 1], "wage": [4, 8, 2, 2, 7], "k": 3},
        "output": 30.66667,
    },
]


@pytest.mark.sol857
def test_run():
    for case in cases:
        assert (
            round(
                Solution.min_cost_to_hire_workers(
                    quality=case["input"]["quality"],
                    wage=case["input"]["wage"],
                    k=case["input"]["k"],
                ),
                5,
            )
            == case["output"]
        )
