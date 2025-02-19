import pytest
from solutions.sol_1415 import Solution


cases = [
    {
        "input": {"n": 1, "k": 3},
        "output": "c",
    },
    {
        "input": {"n": 1, "k": 4},
        "output": "",
    },
    {
        "input": {"n": 3, "k": 9},
        "output": "cab",
    },
]


@pytest.mark.sol1415
def test_run():
    for case in cases:
        assert (
            Solution.get_happy_string(
                n=case["input"]["n"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
