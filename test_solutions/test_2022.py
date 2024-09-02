import pytest
from solutions.sol_2022 import Solution


cases = [
    {
        "input": {"original": [1, 2, 3, 4], "m": 2, "n": 2},
        "output": [[1, 2], [3, 4]],
    },
    {
        "input": {"original": [1, 2, 3], "m": 1, "n": 3},
        "output": [[1, 2, 3]],
    },
    {
        "input": {"original": [1, 2], "m": 1, "n": 1},
        "output": [],
    },
]


@pytest.mark.sol2022
def test_run():
    for case in cases:
        assert (
            Solution.construct_2d_array(
                original=case["input"]["original"],
                n=case["input"]["n"],
                m=case["input"]["m"],
            )
            == case["output"]
        )
