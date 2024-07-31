import pytest
from solutions.sol_1105 import Solution


cases = [
    {
        "input": {
            "books": [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], "shelfWidth": 4
        },
        "output": 6,
    },
    {
        "input": {
            "books": [[1, 3], [2, 4], [3, 2]], "shelfWidth": 6
        },
        "output": 4,
    },
]


@pytest.mark.sol1105
def test_run():
    for case in cases:
        assert (
            Solution.min_height_shelves(
                books=case["input"]["books"],
                shelf_width=case["input"]["shelfWidth"],
            )
            == case["output"]
        )
