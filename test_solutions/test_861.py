import pytest
from solutions.sol_861 import Solution

cases = [
    {
        "input": {
            "grid": [[0,0,1,1],[1,0,1,0],[1,1,0,0]],
        },
        "output": 39,
    },
    {
        "input": {
            "grid": [[0]],
        },
        "output": 1,
    },
]


@pytest.mark.sol861
def test_run():
    for case in cases:
        assert (
                Solution.matrix_score(
                    grid=case["input"]["grid"],
                )
                == case["output"]
        )
