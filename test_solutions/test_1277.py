import pytest
from solutions.sol_1277 import Solution


cases = [
    {
        "input": {"matrix": [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]},
        "output": 15,
    },
    {
        "input": {"matrix": [[1, 0, 1], [1, 1, 0], [1, 1, 0]]},
        "output": 7,
    },
]


@pytest.mark.sol1277
def test_run():
    for case in cases:
        assert (
            Solution.count_squares(
                matrix=case["input"]["matrix"],
            )
            == case["output"]
        )
