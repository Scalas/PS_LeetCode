import pytest
from solutions.sol_2285 import Solution


cases = [
    {
        "input": {"n": 5, "roads": [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]},
        "output": 43,
    },
    {
        "input": {"n": 5, "roads": [[0, 3], [2, 4], [1, 3]]},
        "output": 20,
    },
]


@pytest.mark.sol2285
def test_run():
    for case in cases:
        assert (
            Solution.maximum_importance(
                roads=case["input"]["roads"],
                n=case["input"]["n"],
            )
            == case["output"]
        )
