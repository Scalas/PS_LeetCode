import pytest
from solutions.sol_664 import Solution

cases = [
    {
        "input": {
            "s": "aaabbb",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "aba",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "bacdadacbdbcabd",
        },
        "output": 9,
    },
    {
        "input": {
            "s": "xfqsduwlrrbvtglkdjvplhgtwmjkocjomwkamntkpskipyshnnsivshulwsebzswogvjtevsmjxrfgyxhsvfnptytkwaguvsiqqu",
        },
        "output": 73,
    },
]


@pytest.mark.sol_664
def test_run():
    for case in cases:
        assert (
            Solution.strange_printer(
                s=case["input"]["s"],
            )
            == case["output"]
        )
