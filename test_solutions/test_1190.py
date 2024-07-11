import pytest
from solutions.sol_1190 import Solution


cases = [
    {
        "input": {"s": "(abcd)"},
        "output": "dcba",
    },
    {
        "input": {"s": "(u(love)i)"},
        "output": "iloveu",
    },
    {
        "input": {"s": "(ed(et(oc))el)"},
        "output": "leetcode",
    },
]


@pytest.mark.sol1190
def test_run():
    for case in cases:
        assert (
            Solution.reverse_parentheses(
                s=case["input"]["s"],
            )
            == case["output"]
        )
