import pytest
from solutions.sol_885 import Solution


cases = [
    # {
    #     "input": {
    #         "rows": 1, "cols": 4, "rStart": 0, "cStart": 0
    #     },
    #     "output": [[0, 0], [0, 1], [0, 2], [0, 3]],
    # },
    {
        "input": {"rows": 5, "cols": 6, "rStart": 1, "cStart": 4},
        "output": [
            [1, 4],
            [1, 5],
            [2, 5],
            [2, 4],
            [2, 3],
            [1, 3],
            [0, 3],
            [0, 4],
            [0, 5],
            [3, 5],
            [3, 4],
            [3, 3],
            [3, 2],
            [2, 2],
            [1, 2],
            [0, 2],
            [4, 5],
            [4, 4],
            [4, 3],
            [4, 2],
            [4, 1],
            [3, 1],
            [2, 1],
            [1, 1],
            [0, 1],
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
        ],
    },
]


@pytest.mark.sol885
def test_run():
    for case in cases:
        assert (
            Solution.spiral_matrix_3(
                rStart=case["input"]["rStart"],
                rows=case["input"]["rows"],
                cols=case["input"]["cols"],
                cStart=case["input"]["cStart"],
            )
            == case["output"]
        )
