import pytest
from solutions.sol_2683 import Solution


cases = [
    {
        "input": {"derived": [1, 1, 0]},
        "output": True,
    },
    {
        "input": {"derived": [1, 1]},
        "output": True,
    },
    {
        "input": {"derived": [1, 0]},
        "output": False,
    },
]


@pytest.mark.sol2683
def test_run():
    for case in cases:
        assert (
            Solution.does_valid_array_exist(
                derived=case["input"]["derived"],
            )
            == case["output"]
        )
