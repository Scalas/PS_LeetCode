import pytest
from solutions.sol_2976 import Solution


cases = [
    {
        "input": {
            "source": "abcd",
            "target": "acbe",
            "original": ["a", "b", "c", "c", "e", "d"],
            "changed": ["b", "c", "b", "e", "b", "e"],
            "cost": [2, 5, 5, 1, 2, 20],
        },
        "output": 28,
    },
    {
        "input": {
            "source": "aaaa",
            "target": "bbbb",
            "original": ["a", "c"],
            "changed": ["c", "b"],
            "cost": [1, 2],
        },
        "output": 12,
    },
    {
        "input": {
            "source": "abcd",
            "target": "abce",
            "original": ["a"],
            "changed": ["e"],
            "cost": [10000],
        },
        "output": -1,
    },
]


@pytest.mark.sol2976
def test_run():
    for case in cases:
        assert (
            Solution.minimum_cost(
                original=case["input"]["original"],
                target=case["input"]["target"],
                source=case["input"]["source"],
                cost=case["input"]["cost"],
                changed=case["input"]["changed"],
            )
            == case["output"]
        )
