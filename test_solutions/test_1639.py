import pytest
from solutions.sol_1639 import Solution

cases = [
    {
        "input": {
            "words": ["acca", "bbbb", "caca"],
            "target": "aba",
        },
        "output": 6,
    },
    {
        "input": {
            "words": ["abba", "baab"],
            "target": "bab",
        },
        "output": 4,
    },
]


@pytest.mark.sol1639
def test_run():
    for case in cases:
        assert (
            Solution.num_ways(
                words=case["input"]["words"], target=case["input"]["target"]
            )
            == case["output"]
        )
