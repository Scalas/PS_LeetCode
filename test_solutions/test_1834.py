import pytest
from solutions.sol_1834 import Solution

cases = [
    {"input": {"tasks": [[1, 2], [2, 4], [3, 2], [4, 1]]}, "output": [0, 2, 3, 1]},
    {
        "input": {"tasks": [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]},
        "output": [4, 3, 2, 0, 1],
    },
    {
        "input": {
            "tasks": [
                [35, 36],
                [11, 7],
                [15, 47],
                [34, 2],
                [47, 19],
                [16, 14],
                [19, 8],
                [7, 34],
                [38, 15],
                [16, 18],
                [27, 22],
                [7, 15],
                [43, 2],
                [10, 5],
                [5, 4],
                [3, 11],
            ]
        },
        "output": [15, 14, 13, 1, 6, 3, 5, 12, 8, 11, 9, 4, 10, 7, 0, 2],
    },
]


@pytest.mark.sol1834
def test_run():
    for case in cases:
        assert Solution.get_order(tasks=case["input"]["tasks"]) == case["output"]
