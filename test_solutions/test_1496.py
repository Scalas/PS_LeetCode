import pytest
from solutions.sol_1496 import Solution

cases = [
    {
        "input": {
            "path": "NES",
        },
        "output": False,
    },
    {
        "input": {
            "path": "NESWW",
        },
        "output": True,
    },
]


@pytest.mark.sol1496
def test_run():
    for case in cases:
        assert (
            Solution.is_path_crossing(
                path=case["input"]["path"],
            )
            == case["output"]
        )
