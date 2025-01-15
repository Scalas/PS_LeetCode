import pytest
from solutions.sol_2429 import Solution


cases = [
    {
        "input": {"num1": 3, "num2": 5},
        "output": 3,
    },
    {
        "input": {"num1": 1, "num2": 12},
        "output": 3,
    },
    {
        "input": {"num1": 8, "num2": 75},
        "output": 15,
    },
    {
        "input": {"num1": 25, "num2": 72},
        "output": 24,
    },
]


@pytest.mark.sol2429
def test_run():
    for case in cases:
        assert (
            Solution.minimize_xor(
                num1=case["input"]["num1"],
                num2=case["input"]["num2"],
            )
            == case["output"]
        )
