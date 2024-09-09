import pytest

from converter.leet_code_utils import list_to_linked_list
from solutions.sol_2326 import Solution


cases = [
    {
        "input": {"m": 3, "n": 5, "head": [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]},
        "output": [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]],
    },
    {
        "input": {"m": 1, "n": 4, "head": [0, 1, 2]},
        "output": [[0, 1, 2, -1]],
    },
]


@pytest.mark.sol2326
def test_run():
    for case in cases:
        assert (
            Solution.spiral_matrix(
                head=list_to_linked_list(case["input"]["head"]),
                n=case["input"]["n"],
                m=case["input"]["m"],
            )
            == case["output"]
        )
