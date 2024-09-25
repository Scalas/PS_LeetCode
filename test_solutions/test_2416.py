import pytest
from solutions.sol_2416 import Solution


cases = [
    {
        "input": {"words": ["abc", "ab", "bc", "b"]},
        "output": [5, 4, 3, 2],
    },
    {
        "input": {"words": ["abcd"]},
        "output": [4],
    },
]


@pytest.mark.sol2416
def test_run():
    for case in cases:
        assert (
            Solution.sum_prefix_scores(
                words=case["input"]["words"],
            )
            == case["output"]
        )
