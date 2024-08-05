import pytest
from solutions.sol_2053 import Solution


cases = [
    {
        "input": {"arr": ["d", "b", "c", "b", "c", "a"], "k": 2},
        "output": "a",
    },
    {
        "input": {"arr": ["aaa", "aa", "a"], "k": 1},
        "output": "aaa",
    },
    {
        "input": {"arr": ["a", "b", "a"], "k": 3},
        "output": "",
    },
]


@pytest.mark.sol2053
def test_run():
    for case in cases:
        assert (
            Solution.kth_distinct(
                arr=case["input"]["arr"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
