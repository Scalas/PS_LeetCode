import pytest
from solutions.sol_2109 import Solution


cases = [
    {
        "input": {"s": "LeetcodeHelpsMeLearn", "spaces": [8, 13, 15]},
        "output": "Leetcode Helps Me Learn",
    },
    {
        "input": {"s": "icodeinpython", "spaces": [1, 5, 7, 9]},
        "output": "i code in py thon",
    },
    {
        "input": {"s": "spacing", "spaces": [0, 1, 2, 3, 4, 5, 6]},
        "output": " s p a c i n g",
    },
]


@pytest.mark.sol2109
def test_run():
    for case in cases:
        assert (
            Solution.add_spaces(
                spaces=case["input"]["spaces"],
                s=case["input"]["s"],
            )
            == case["output"]
        )
