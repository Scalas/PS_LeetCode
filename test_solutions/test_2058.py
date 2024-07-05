import pytest

from converter.leet_code_utils import list_to_linked_list
from solutions.sol_2058 import Solution


cases = [
    {
        "input": {"head": [3, 1]},
        "output": [-1, -1],
    },
    {
        "input": {"head": [5, 3, 1, 2, 5, 1, 2]},
        "output": [1, 3],
    },
    {
        "input": {"head": [1, 3, 2, 2, 3, 2, 2, 2, 7]},
        "output": [3, 3],
    },
]


@pytest.mark.sol2058
def test_run():
    for case in cases:
        assert (
            Solution.nodes_between_critical_points(
                head=list_to_linked_list(case["input"]["head"]),
            )
            == case["output"]
        )
