import pytest
from solutions.sol_1518 import Solution


cases = [
    {
        "input": {"num_bottles": 9, "num_exchange": 3},
        "output": 13,
    },
    {
        "input": {"num_bottles": 15, "num_exchange": 4},
        "output": 19,
    },
]


@pytest.mark.sol1518
def test_run():
    for case in cases:
        assert (
            Solution.num_bottles(
                num_bottles=case["input"]["num_bottles"],
                num_exchange=case["input"]["num_exchange"],
            )
            == case["output"]
        )
