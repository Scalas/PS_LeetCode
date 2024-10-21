import pytest
from solutions.sol_1106 import Solution


cases = [
    {
        "input": {"expression": "&(|(f))"},
        "output": False,
    },
    {
        "input": {"expression": "|(f, f, f, t)"},
        "output": True,
    },
    {
        "input": {"expression": "!(&(f, t))"},
        "output": True,
    },
]


@pytest.mark.sol1106
def test_run():
    for case in cases:
        assert (
            Solution.parse_bool_expr(
                expression=case["input"]["expression"],
            )
            == case["output"]
        )
