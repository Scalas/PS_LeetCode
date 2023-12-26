import pytest
from solutions.sol_1155 import Solution

cases = [
    {"input": {"n": 1, "k": 6, "target": 3}, "output": 1},
    {"input": {"n": 2, "k": 6, "target": 7}, "output": 6},
    {"input": {"n": 30, "k": 30, "target": 500}, "output": 222616187},
]


@pytest.mark.sol1155
def test_run():
    for case in cases:
        assert (
            Solution.num_rolls_to_target(
                n=case["input"]["n"],
                k=case["input"]["k"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
