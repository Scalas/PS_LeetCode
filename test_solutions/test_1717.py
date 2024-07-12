import pytest
from solutions.sol_1717 import Solution


cases = [
    {
        "input": {"s": "cdbcbbaaabab", "x": 4, "y": 5},
        "output": 19,
    },
    {
        "input": {"s": "aabbaaxybbaabb", "x": 5, "y": 4},
        "output": 20,
    },
]


@pytest.mark.sol1717
def test_run():
    for case in cases:
        assert (
            Solution.maximum_gain(
                s=case["input"]["s"],
                y=case["input"]["y"],
                x=case["input"]["x"],
            )
            == case["output"]
        )
