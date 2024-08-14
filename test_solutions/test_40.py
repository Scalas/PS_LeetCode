import pytest
from solutions.sol_40 import Solution


cases = [
    {
        "input": {"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8},
        "output": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
    },
    {
        "input": {"candidates": [2, 5, 2, 1, 2], "target": 5},
        "output": [[1, 2, 2], [5]],
    },
]


@pytest.mark.sol40
def test_run():
    for case in cases:
        assert sorted(
            Solution.combination_sum2(
                target=case["input"]["target"],
                candidates=case["input"]["candidates"],
            )
        ) == sorted(case["output"])
