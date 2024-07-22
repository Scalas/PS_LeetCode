import pytest
from solutions.sol_2418 import Solution


cases = [
    {
        "input": {
            "names": ["Mary", "John", "Emma"], "heights": [180, 165, 170]
        },
        "output": ["Mary", "Emma", "John"],
    },
    {
        "input": {
            "names": ["Alice", "Bob", "Bob"], "heights": [155, 185, 150]
        },
        "output": ["Bob", "Alice", "Bob"],
    },
]


@pytest.mark.sol2418
def test_run():
    for case in cases:
        assert (
            Solution.sort_people(
                heights=case["input"]["heights"],
                names=case["input"]["names"],
            )
            == case["output"]
        )
