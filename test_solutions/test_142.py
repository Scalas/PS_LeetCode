import pytest

from converter.leet_code_utils import list_to_cyclic_linked_list
from solutions.sol_142 import Solution

cases = [
    {"input": {"head": [3, 2, 0, -4], "pos": 1}, "output": 1},
    {"input": {"head": [1, 2], "pos": 0}, "output": 0},
    {"input": {"head": [1], "pos": -1}, "output": -1},
]


@pytest.mark.sol142
def test_run():
    for case in cases:
        head, expected = list_to_cyclic_linked_list(
            case["input"]["head"], case["input"]["pos"]
        )

        assert (
            Solution.detect_cycle(
                head=head,
            )
            == expected
        )
