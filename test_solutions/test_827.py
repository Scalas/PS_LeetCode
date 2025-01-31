import pytest
from solutions.sol_827 import Solution


cases = [
    {
        "input": {"grid": [[1, 0], [0, 1]]},
        "output": 3,
    },
    {
        "input": {"grid": [[1, 1], [1, 0]]},
        "output": 4,
    },
    {
        "input": {"grid": [[1, 1], [1, 1]]},
        "output": 4,
    },
]


@pytest.mark.sol827
def test_run():
    for case in cases:
        assert (
            Solution.largest_is_land(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
