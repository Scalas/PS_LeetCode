import pytest
from solutions.sol_920 import Solution

cases = [
    {
        "input": {
            "n": 3,
            "goal": 3,
            "k": 1,
        },
        "output": 6,
    },
    {
        "input": {
            "n": 2,
            "goal": 3,
            "k": 0,
        },
        "output": 6,
    },
    {
        "input": {
            "n": 2,
            "goal": 3,
            "k": 1,
        },
        "output": 2,
    },
    {
        "input": {
            "n": 2,
            "goal": 4,
            "k": 0,
        },
        "output": 14,
    },
    {
        "input": {
            "n": 3,
            "goal": 4,
            "k": 0,
        },
        "output": 36,
    },
]


@pytest.mark.sol920
def test_run():
    for case in cases:
        assert (
            Solution.num_music_playlists(
                n=case["input"]["n"],
                goal=case["input"]["goal"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
