import pytest
from solutions.sol_786 import Solution

cases = [
    {
        "input": {"arr": [1, 2, 3, 5], "k": 3},
        "output": [2, 5],
    },
    {
        "input": {"arr": [1, 7], "k": 1},
        "output": [1, 7],
    },
]


@pytest.mark.sol_786
def test_run():
    for case in cases:
        assert (
            Solution.kth_smallest_prime_fraction(
                arr=case["input"]["arr"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
