import pytest
from solutions.sol_1249 import Solution

cases = [
    {
        "input": {
            "s": "lee(t(c)o)de)",
        },
        "output": "lee(t(c)o)de",
    },
    {
        "input": {
            "s": "a)b(c)d",
        },
        "output": "ab(c)d",
    },
    {
        "input": {
            "s": "))((",
        },
        "output": "",
    },
]


@pytest.mark.sol1249
def test_run():
    for case in cases:
        assert (
            Solution.min_remove_to_make_valid(
                s=case["input"]["s"],
            )
            == case["output"]
        )
