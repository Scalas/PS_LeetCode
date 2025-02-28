import pytest
from solutions.sol_1092 import Solution


cases = [
    {
        "input": {"str1": "abac", "str2": "cab"},
        "output": "cabac",
    },
    {
        "input": {"str1": "aaaaaaaa", "str2": "aaaaaaaa"},
        "output": "aaaaaaaa",
    },
    {
        "input": {"str1": "acxyzbc", "str2": "abcxyz"},
        "output": "abcxyzbc",
    },
    {
        "input": {"str1": "ababaabbbb", "str2": "cbcbacaab"},
        "output": "acbacbacaabbbb",
    },
]


@pytest.mark.sol1092
def test_run():
    for case in cases:
        assert (
            Solution.shortest_common_super_sequence(
                str2=case["input"]["str2"],
                str1=case["input"]["str1"],
            )
            == case["output"]
        )
