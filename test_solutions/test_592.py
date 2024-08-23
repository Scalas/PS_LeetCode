import pytest
from solutions.sol_592 import Solution


cases = [
    {
        "input": {"expression": "-1/2+1/2"},
        "output": "0/1",
    },
    {
        "input": {"expression": "-1/2+1/2+1/3"},
        "output": "1/3",
    },
    {
        "input": {"expression": "1/3-1/2"},
        "output": "-1/6",
    },
]


@pytest.mark.sol592
def test_run():
    for case in cases:
        assert (
            Solution.fraction_addition(
                expression=case["input"]["expression"],
            )
            == case["output"]
        )
