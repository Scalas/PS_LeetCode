import pytest

from converter.leet_code_utils import list_to_linked_list, list_to_cyclic_linked_list
from solutions.sol_141 import Solution

cases = [
    {
        "input": {
            "head": [3, 2, 0, -4],
            "pos": 1,
        },
        "output": True,
    },
    {
        "input": {
            "head": [1, 2],
            "pos": 0,
        },
        "output": True,
    },
    {
        "input": {
            "head": [1],
            "pos": -1,
        },
        "output": False,
    },
]


@pytest.mark.sol141
def test_run():
    for case in cases:
        assert (
            Solution.has_cycle(
                head=list_to_cyclic_linked_list(
                    case["input"]["head"], case["input"]["pos"]
                )[0]
            )
            == case["output"]
        )
