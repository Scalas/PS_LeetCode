import pytest
from solutions.sol_2825 import Solution


cases = [
    {
        "input": {"str1": "abc", "str2": "ad"},
        "output": True,
    },
    {
        "input": {"str1": "zc", "str2": "ad"},
        "output": True,
    },
    {
        "input": {"str1": "ab", "str2": "d"},
        "output": False,
    },
]


@pytest.mark.sol2825
def test_run():
    for case in cases:
        assert (
            Solution.can_make_subsequence(
                str1=case["input"]["str1"],
                str2=case["input"]["str2"],
            )
            == case["output"]
        )
