import pytest
from solutions.sol_661 import Solution

cases = [
    {
        "input": {
            "img": [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        },
        "output": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    },
    {
        "input": {
            "img": [[100, 200, 100], [200, 50, 200], [100, 200, 100]],
        },
        "output": [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
    },
]


@pytest.mark.sol_661
def test_run():
    for case in cases:
        assert (
            Solution.image_smoother(
                img=case["input"]["img"],
            )
            == case["output"]
        )
