import pytest
from solutions.sol_1894 import Solution


cases = [
    {
        "input": {"chalk": [5, 1, 5], "k": 22},
        "output": 0,
    },
    {
        "input": {"chalk": [3, 4, 1, 2], "k": 25},
        "output": 1,
    },
]


@pytest.mark.sol1894
def test_run():
    for case in cases:
        assert (
            Solution.chalk_replacer(
                chalk=case["input"]["chalk"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
