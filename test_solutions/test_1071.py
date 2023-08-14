import pytest
from solutions.sol_1071 import Solution

cases = [
    {
        "input": {
            "str1": "ABCABC",
            "str2": "ABC",
        },
        "output": "ABC",
    },
    {
        "input": {
            "str1": "ABABAB",
            "str2": "ABAB",
        },
        "output": "AB",
    },
    {
        "input": {
            "str1": "LEET",
            "str2": "CODE",
        },
        "output": "",
    },
]


@pytest.mark.sol1071
def test_run():
    for case in cases:
        assert (
            Solution.gcd_of_strings(
                str1=case["input"]["str1"],
                str2=case["input"]["str2"],
            )
            == case["output"]
        )
