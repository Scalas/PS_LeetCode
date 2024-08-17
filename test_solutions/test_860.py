import pytest
from solutions.sol_860 import Solution


cases = [
    {
        "input": {"bills": [5, 5, 5, 10, 20]},
        "output": True,
    },
    {
        "input": {"bills": [5, 5, 10, 10, 20]},
        "output": False,
    },
]


@pytest.mark.sol860
def test_run():
    for case in cases:
        assert (
            Solution.lemonade_change(
                bills=case["input"]["bills"],
            )
            == case["output"]
        )
