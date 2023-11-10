import pytest

from solutions.sol_1743 import Solution

cases = [
    {
        "input": {
            "adjacent_pairs": [[2, 1], [3, 4], [3, 2]],
        },
        "output": [1, 2, 3, 4],
    },
    {
        "input": {
            "adjacent_pairs": [[4, -2], [1, 4], [-3, 1]],
        },
        "output": [-2, 4, 1, -3],
    },
    {
        "input": {
            "adjacent_pairs": [[100000, -100000]],
        },
        "output": [100000, -100000],
    },
]


@pytest.mark.sol1743
def test_run():
    for case in cases:
        assert (
            Solution.restore_array(
                adjacent_pairs=case["input"]["adjacent_pairs"],
            )
            == case["output"]
        )
