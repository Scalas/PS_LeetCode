import pytest
from solutions.sol_1792 import Solution


cases = [
    {
        "input": {"classes": [[1, 2], [3, 5], [2, 2]], "extra_students": 2},
        "output": 0.78333,
    },
    {
        "input": {"classes": [[2, 4], [3, 9], [4, 5], [2, 10]], "extra_students": 4},
        "output": 0.53485,
    },
]


@pytest.mark.sol1792
def test_run():
    for case in cases:
        assert (
            round(
                Solution.max_average_ratio(
                    extra_students=case["input"]["extra_students"],
                    classes=case["input"]["classes"],
                ),
                5,
            )
            == case["output"]
        )
