import pytest
from solutions.sol_2559 import Solution


cases = [
    {
        "input": {
            "words": ["aba", "bcb", "ece", "aa", "e"],
            "queries": [[0, 2], [1, 4], [1, 1]],
        },
        "output": [2, 3, 0],
    },
    {
        "input": {"words": ["a", "e", "i"], "queries": [[0, 2], [0, 1], [2, 2]]},
        "output": [3, 2, 1],
    },
]


@pytest.mark.sol2559
def test_run():
    for case in cases:
        assert (
            Solution.vowel_strings(
                words=case["input"]["words"],
                queries=case["input"]["queries"],
            )
            == case["output"]
        )
