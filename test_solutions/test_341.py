import pytest

from converter.leet_code_utils import map_list_to_nested_integer_list
from solutions.sol_341 import NestedIterator

cases = [
    {"input": {"nested_list": [[1, 1], 2, [1, 1]]}, "output": [1, 1, 2, 1, 1]},
    {"input": {"nested_list": [1, [4, [6]]]}, "output": [1, 4, 6]},
]


@pytest.mark.sol_341
def test_run():
    for case in cases:
        it = NestedIterator(
            nested_list=map_list_to_nested_integer_list(case["input"]["nested_list"])
        )
        res = []
        while it.has_next():
            res.append(it.next())
        assert res == case["output"]
