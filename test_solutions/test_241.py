import pytest
from solutions.sol_241 import Solution


cases = [
    {
        "input": {"expression": "2-1-1"},
        "output": [0, 2],
    },
    {
        "input": {"expression": "2*3-4*5"},
        "output": [-34, -14, -10, -10, 10],
    },
]


@pytest.mark.sol241
def test_run():
    for case in cases:
        assert sorted(
            Solution.diffWaysToCompute(
                expression=case["input"]["expression"],
            )
        ) == sorted(case["output"])
