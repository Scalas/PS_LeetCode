import pytest
from solutions.sol_2579 import Solution


cases = [
    {
        "input": {
            "n": 1
        },
        "output": 1,
    },
    {
        "input": {
            "n": 2
        },
        "output": 5,
    },
]


@pytest.mark.sol2579
def test_run():
    for case in cases:
        assert (
            Solution.colored_cells(
                n=case["input"]["n"],
            )
            == case["output"]
        )
