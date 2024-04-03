import pytest
from solutions.sol_79 import Solution

cases = [
    {
        "input": {
            "board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "word": "ABCCED",
        },
        "output": True,
    },
    {
        "input": {
            "board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "word": "SEE",
        },
        "output": True,
    },
    {
        "input": {
            "board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "word": "ABCB",
        },
        "output": False,
    },
    {
        "input": {
            "board": [["a", "a"]],
            "word": "aaa",
        },
        "output": False,
    },
    {
        "input": {
            "board": [["a", "b"], ["c", "d"]],
            "word": "acdb",
        },
        "output": True,
    },
    {
        "input": {
            "board": [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
            "word": "ABCESEEEFS",
        },
        "output": True,
    },
]


@pytest.mark.sol79
def test_run():
    for case in cases:
        assert (
            Solution.exist(
                board=case["input"]["board"],
                word=case["input"]["word"],
            )
            == case["output"]
        )
