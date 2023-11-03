import pytest
from solutions.sol_1441 import Solution

cases = [
    {
        "input": {
            "target": [1, 3],
            "n": 3,
        },
        "output": ["Push", "Push", "Pop", "Push"],
    },
    {
        "input": {
            "target": [1, 2, 3],
            "n": 3,
        },
        "output": ["Push", "Push", "Push"],
    },
    {
        "input": {
            "target": [1, 2],
            "n": 4,
        },
        "output": ["Push", "Push"],
    },
]


@pytest.mark.sol1441
def test_run():
    for case in cases:
        assert (
            Solution.build_array(target=case["input"]["target"], n=case["input"]["n"])
            == case["output"]
        )
