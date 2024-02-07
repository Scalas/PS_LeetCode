import pytest
from solutions.sol_451 import Solution

cases = [
    {
        "input": {
            "s": "tree",
        },
        "output": "eert",
    },
    {
        "input": {
            "s": "cccaaa",
        },
        "output": "aaaccc",
    },
    {
        "input": {
            "s": "Aabb",
        },
        "output": "bbAa",
    },
]


@pytest.mark.sol451
def test_run():
    for case in cases:
        assert (
            Solution.frequency_sort(
                s=case["input"]["s"],
            )
            == case["output"]
        )
