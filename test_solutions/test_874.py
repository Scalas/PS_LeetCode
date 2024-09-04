import pytest
from solutions.sol_874 import Solution


cases = [
    {
        "input": {"commands": [4, -1, 3], "obstacles": []},
        "output": 25,
    },
    {
        "input": {"commands": [4, -1, 4, -2, 4], "obstacles": [[2, 4]]},
        "output": 65,
    },
    {
        "input": {"commands": [6, -1, -1, 6], "obstacles": []},
        "output": 36,
    },
]


@pytest.mark.sol874
def test_run():
    for case in cases:
        assert (
            Solution.robot_sim(
                commands=case["input"]["commands"],
                obstacles=case["input"]["obstacles"],
            )
            == case["output"]
        )
