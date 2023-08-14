import pytest
from solutions.sol_2305 import Solution

cases = [
    {
        "input": {
            "cookies": [8, 15, 10, 20, 8],
            "k": 2,
        },
        "output": 31,
    },
    {
        "input": {
            "cookies": [6, 1, 3, 2, 2, 4, 1, 2],
            "k": 3,
        },
        "output": 7,
    },
]


@pytest.mark.sol_2305
def test_run():
    for case in cases:
        assert (
            Solution.distribute_cookies(
                cookies=case["input"]["cookies"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
