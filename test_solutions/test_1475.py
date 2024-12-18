import pytest
from solutions.sol_1475 import Solution


cases = [
    {
        "input": {"prices": [8, 4, 6, 2, 3]},
        "output": [4, 2, 4, 2, 3],
    },
    {
        "input": {"prices": [1, 2, 3, 4, 5]},
        "output": [1, 2, 3, 4, 5],
    },
    {
        "input": {"prices": [10, 1, 1, 6]},
        "output": [9, 0, 1, 6],
    },
]


@pytest.mark.sol1475
def test_run():
    for case in cases:
        assert (
            Solution.final_prices(
                prices=case["input"]["prices"],
            )
            == case["output"]
        )
