import pytest
from solutions.sol_873 import Solution


cases = [
    {
        "input": {"arr": [1, 2, 3, 4, 5, 6, 7, 8]},
        "output": 5,
    },
    {
        "input": {"arr": [1, 3, 7, 11, 12, 14, 18]},
        "output": 3,
    },
]


@pytest.mark.sol873
def test_run():
    for case in cases:
        assert (
            Solution.len_longest_fib_subseq(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
