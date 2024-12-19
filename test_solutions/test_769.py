import pytest
from solutions.sol_769 import Solution


cases = [
    {
        "input": {"arr": [4, 3, 2, 1, 0]},
        "output": 1,
    },
    {
        "input": {"arr": [1, 0, 2, 3, 4]},
        "output": 4,
    },
]


@pytest.mark.sol769
def test_run():
    for case in cases:
        assert (
            Solution.max_chunks_to_sorted(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
