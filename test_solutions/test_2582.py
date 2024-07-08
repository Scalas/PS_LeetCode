import pytest
from solutions.sol_2582 import Solution


cases = [
    {
        "input": {"n": 4, "time": 5},
        "output": 2,
    },
    {
        "input": {"n": 3, "time": 2},
        "output": 3,
    },
]


@pytest.mark.sol2582
def test_run():
    for case in cases:
        assert (
            Solution.pass_the_pillow(
                n=case["input"]["n"],
                time=case["input"]["time"],
            )
            == case["output"]
        )
