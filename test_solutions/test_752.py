import pytest
from solutions.sol_752 import Solution

cases = [
    {
        "input": {
            "dead_ends": ["0201", "0101", "0102", "1212", "2002"],
            "target": "0202",
        },
        "output": 6,
    },
    {
        "input": {
            "dead_ends": ["8888"],
            "target": "0009",
        },
        "output": 1,
    },
    {
        "input": {
            "dead_ends": [
                "8887",
                "8889",
                "8878",
                "8898",
                "8788",
                "8988",
                "7888",
                "9888",
            ],
            "target": "8888",
        },
        "output": -1,
    },
    {
        "input": {
            "dead_ends": ["0000"],
            "target": "8888",
        },
        "output": -1,
    },
]


@pytest.mark.sol_752
def test_run():
    for case in cases:
        assert (
            Solution.open_lock(
                dead_ends=case["input"]["dead_ends"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
