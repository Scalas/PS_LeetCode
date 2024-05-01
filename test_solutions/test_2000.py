import pytest
from solutions.sol_2000 import Solution

cases = [
    {
        "input": {"word": "abcdefd", "ch": "d"},
        "output": "dcbaefd",
    },
    {
        "input": {"word": "xyxzxe", "ch": "z"},
        "output": "zxyxxe",
    },
    {
        "input": {"word": "abcd", "ch": "z"},
        "output": "abcd",
    },
]


@pytest.mark.sol_2000
def test_run():
    for case in cases:
        assert (
            Solution.reverse_prefix(
                word=case["input"]["word"],
                ch=case["input"]["ch"],
            )
            == case["output"]
        )
