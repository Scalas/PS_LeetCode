import pytest

from solutions.sol_629 import Solution

cases = [
    {"input": {"n": 3, "k": 0}, "output": 1},
    {"input": {"n": 3, "k": 1}, "output": 2},
]


@pytest.mark.sol_629
def test_run():
    for case in cases:
        assert (
            Solution.k_inverse_pairs(
                n=case["input"]["n"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
