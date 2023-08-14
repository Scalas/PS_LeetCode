import pytest
from solutions.sol_649 import Solution

cases = [
    {
        "input": {
            "senate": "RD",
        },
        "output": "Radiant",
    },
    {
        "input": {
            "senate": "RDD",
        },
        "output": "Dire",
    },
    {
        "input": {
            "senate": "RRDDD",
        },
        "output": "Radiant",
    },
    {
        "input": {
            "senate": "DDRRR",
        },
        "output": "Dire",
    },
    {
        "input": {
            "senate": "DRRDRDRDRDDRDRDR",
        },
        "output": "Radiant",
    },
]


@pytest.mark.sol_649
def test_run():
    for case in cases:
        assert (
            Solution.predict_party_victory(
                senate=case["input"]["senate"],
            )
            == case["output"]
        )
