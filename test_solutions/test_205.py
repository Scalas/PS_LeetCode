import pytest
from solutions.sol_205 import Solution

cases = [
    {
        "input": {
            "s": "paper",
            "t": "title",
        },
        "output": True,
    },
    {
        "input": {
            "s": "foo",
            "t": "bar",
        },
        "output": False,
    },
    {
        "input": {
            "s": "paper",
            "t": "title",
        },
        "output": True,
    },
    {
        "input": {
            "s": "badc",
            "t": "baba",
        },
        "output": False,
    },
]


@pytest.mark.sol205
def test_run():
    for case in cases:
        assert (
            Solution.is_isomorphic(
                s=case["input"]["s"],
                t=case["input"]["t"],
            )
            == case["output"]
        )
