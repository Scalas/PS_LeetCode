import pytest

from converter.leet_code_utils import list_to_linked_list
from solutions.sol_234 import Solution

cases = [
    {
        "input": {
            "head": [1, 2, 2, 1],
        },
        "output": True,
    },
    {
        "input": {
            "head": [1, 2],
        },
        "output": False,
    },
]


@pytest.mark.sol234
def test_run():
    for case in cases:
        assert (
            Solution.is_palindrome(
                head=list_to_linked_list(case["input"]["head"]),
            )
            == case["output"]
        )
