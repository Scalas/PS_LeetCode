import pytest
from solutions.sol_1545 import Solution


cases = [
    {
        "input": {"n": 3, "k": 1},
        "output": "0",
    },
    {
        "input": {"n": 4, "k": 11},
        "output": "1",
    },
]


@pytest.mark.sol1545
def test_run():
    for case in cases:
        assert (
            Solution.find_kth_bit(
                k=case["input"]["k"],
                n=case["input"]["n"],
            )
            == case["output"]
        )
