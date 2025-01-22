import pytest
from solutions.sol_1765 import Solution


cases = [
    {
        "input": {"is_water": [[0, 1], [0, 0]]},
        "output": [[1, 0], [2, 1]],
    },
    {
        "input": {"is_water": [[0, 0, 1], [1, 0, 0], [0, 0, 0]]},
        "output": [[1, 1, 0], [0, 1, 1], [1, 2, 2]],
    },
]


@pytest.mark.sol1765
def test_run():
    for case in cases:
        assert (
            Solution.highest_peak(
                is_water=case["input"]["is_water"],
            )
            == case["output"]
        )
