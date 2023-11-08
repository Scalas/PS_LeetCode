import pytest
from solutions.sol_2849 import Solution

cases = [
    {
        "input": {
            "sx": 2,
            "sy": 4,
            "fx": 7,
            "fy": 7,
            "t": 6,
        },
        "output": True,
    },
    {
        "input": {
            "sx": 3,
            "sy": 1,
            "fx": 7,
            "fy": 3,
            "t": 3,
        },
        "output": False,
    },
    {
        "input": {
            "sx": 1,
            "sy": 2,
            "fx": 1,
            "fy": 2,
            "t": 1,
        },
        "output": False,
    },
    {
        "input": {
            "sx": 1,
            "sy": 2,
            "fx": 1,
            "fy": 2,
            "t": 0,
        },
        "output": True,
    },
]


@pytest.mark.sol_2742
def test_run():
    for case in cases:
        assert (
            Solution.is_reachable_at_time(
                sx=case["input"]["sx"],
                sy=case["input"]["sy"],
                fx=case["input"]["fx"],
                fy=case["input"]["fy"],
                t=case["input"]["t"],
            )
            == case["output"]
        )
